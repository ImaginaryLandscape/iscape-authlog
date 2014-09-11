import logging
# from datetime import datetime, timedelta
from django.core.urlresolvers import reverse, NoReverseMatch
from authlog import models
import authlog

log = logging.getLogger(authlog.AUTHLOG_LOGGER)
log.info('AUTHLOG: BEGIN LOG')
log.info('Using version ' + authlog.get_version())


def hide_passwd(key, value):
    if key == 'password':
        return key, '*********'
    else:
        return key, value


def query2str(items):
    return '\n'.join(['%s=%s' % (hide_passwd(k, v)) for k, v in items])


def get_tracked_models():
    return [tuple([i.lower() for i in j.split('.')]) for j in authlog.AUTHLOG_TRACKED_MODELS]


def watch_login(func):
    """
    Used to decorate the django.contrib.admin.site.login method.
    """

    def decorated_login(request, *args, **kwargs):
        response = func(request, *args, **kwargs)

        if func.__name__ == 'decorated_login':
            # if we're dealing with this function itself, don't bother checking
            # for invalid login attempts.  I suppose there's a bunch of
            # recursion going on here that used to cause one failed login
            # attempt to generate 10+ failed access attempt records (with 3
            # failed attempts each supposedly)
            return response

        if request.method == 'POST':
            # see if the login was successful
            login_unsuccessful = (
                response and
                not response.has_header('location') and
                response.status_code != 302
            )
            if login_check_request(request, login_unsuccessful):
                return response

        return response

    if hasattr(func, 'is_decorated_login'):
        return func

    decorated_login.is_decorated_login = True
    return decorated_login


def login_check_request(request, login_unsuccessful):
    ip = request.META.get('REMOTE_ADDR', '')[:255]
    ip_forward = request.META.get('HTTP_X_FORWARDED_FOR', '')[:255]
    path = request.META.get('PATH_INFO', '<unknown>')[:255]
    accept = request.META.get('HTTP_ACCEPT', '<unknown>')[:255]
    ua = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255]
    # time = datetime.now()
    get = query2str(request.GET.items())

    if authlog.AUTHLOG_SAVE_LOGIN_POST_DATA:
        post = query2str(request.POST.items())
    else:
        post = 'POST data was submitted'

    if login_unsuccessful:
        login_status = "Fail"

        user = 'None'
        if authlog.AUTHLOG_SAVE_BAD_LOGINS:
            access = models.Access.objects.create(user=user,
                                                user_agent=ua,
                                                ip_address=ip,
                                                ip_forward=ip_forward,
                                                get_data=get,
                                                post_data=post,
                                                http_accept=accept,
                                                path_info=path,
                                                )
        return_status = False
    else:
        login_status = "Pass"
        user = request.user

        if authlog.AUTHLOG_SAVE_GOOD_LOGINS:
            access = models.Access.objects.create(
               user=user.username,
               user_agent=ua,
               ip_address=ip,
               ip_forward=ip_forward,
               get_data=get,
               post_data=post,
               http_accept=accept,
               path_info=path,
            )
        return_status = True

    log.info('AUTHLOG: Login %s : ip : %s : ip_forward : %s : path : %s : user : %s ' % (
             login_status, ip, ip_forward or "None", path, user))

    return return_status


class ActionInfo(object):

    def __init__(self, url=None, atype=None):
        self.url = url
        self.atype = atype

    def is_complete(self):
        if self.url and self.atype:
            return True
        else:
            return False


def watch_view(func):
    def decorated_view(request_func, *args, **kwargs):
        response = func(request_func, *args, **kwargs)
        posted = False

        if func.__name__ == 'decorated_view':
            return response

        try:
            request = args[0]
        except:
            request = None   # should never get here

        if not request:
            try:
                request = kwargs.get('request', None)
            except:
                request = None
            user, ip, path, accept, ua, get, post = ('None', '', '<unknown>', '<unknown>', '<unknown>', '', '')
            current_path = '/'
        else:
            current_path = request.path_info
            user = request.user
            ip = request.META.get('REMOTE_ADDR', '')[:255]
            ip_forward = request.META.get('HTTP_X_FORWARDED_FOR', '')[:255]
            path = request.META.get('PATH_INFO', '<unknown>')[:255]
            accept = request.META.get('HTTP_ACCEPT', '<unknown>')[:255]
            ua = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255]
            get = query2str(request.GET.items())
            post = query2str(request.POST.items())

        if request.method == 'POST':
            posted = True

        if posted and not authlog.AUTHLOG_SAVE_VIEW_POST_DATA:
            post = "POST data was submitted"

        tracked_models = get_tracked_models()
        # tracked_urls = []

        action = ActionInfo()

        for tmodel in tracked_models:
            try:
                app = tmodel[0]
                model = tmodel[1]
            except IndexError:
                pass  # should only get here if someone does not specify correct tracked models
                raise NameError("You settings file does not have a properly formated list " +
                                "of AUTHLOG_TRACKED_MODELS.  Entries must be formatted app.model")

            try:
                first_arg = args[1]
            except IndexError:
                first_arg = None

            try:
                if first_arg:
                    if current_path == reverse('admin:%s_%s_change' % (app, model), args=(first_arg,)):
                        action.url = current_path
                        action.atype = models.ACTION_TYPE['SUBMIT_CHANGE'] if posted else models.ACTION_TYPE['VIEW_CHANGE']
                        break
                    elif current_path == reverse('admin:%s_%s_delete' % (app, model), args=(first_arg,)):
                        action.url = current_path
                        action.atype = models.ACTION_TYPE['SUBMIT_DELETE'] if posted else models.ACTION_TYPE['VIEW_DELETE']
                        break
                    elif current_path == reverse('admin:%s_%s_history' % (app, model), args=(first_arg,)):
                        action.url = current_path
                        action.atype = models.ACTION_TYPE['VIEW_HISTORY']
                        break
                else:
                    if current_path == reverse('admin:%s_%s_changelist' % (app, model),):
                        action.url = current_path
                        action.atype = models.ACTION_TYPE['VIEW_LIST']
                        break
                    elif current_path == reverse('admin:%s_%s_add' % (app, model),):
                        action.url = current_path
                        action.atype = models.ACTION_TYPE['VIEW_ADD'] if posted else models.ACTION_TYPE['SUBMIT_ADD']
                        break

            except NoReverseMatch:
                # pass  # should only get here if tracked_models is wrong (no view associated)
                raise NoReverseMatch

        if action.is_complete():
            models.AccessPage.objects.create(
               user=user.username, user_agent=ua, ip_address=ip, ip_forward=ip_forward,
               get_data=get, post_data=post, http_accept=accept,
               path_info=action.url, action_type=action.atype,
            )

        return response

    # if hasattr(func, 'is_decorated_view'):
        # return func

    # decorated_view.is_decorated_view = True
    return decorated_view
