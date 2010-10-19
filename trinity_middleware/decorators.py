from django.conf import settings
from datetime import datetime, timedelta
from trinity_middleware.models import Access

def hide_passwd(key, value):
    if key == 'password':
        return key, '*********'
    else:
        return key, value

def query2str(items):
    return '\n'.join(['%s=%s' % (hide_passwd(k, v)) for k,v in items ])

def watch_login(func):
    """
    Used to decorate the django.contrib.admin.site.login method.
    """

    def decorated_login(request, *args, **kwargs):
        # share some useful information
        #if func.__name__ != 'decorated_login' and VERBOSE:
            #log.info('AXES: Calling decorated function: %s' % func.__name__)
            #if args: log.info('args: %s' % args)
            #if kwargs: log.info('kwargs: %s' % kwargs)
            #pass
        # call the login function
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
            if check_request(request, login_unsuccessful):
                return response

        return response

    return decorated_login

def check_request(request, login_unsuccessful):
    ip = request.META.get('REMOTE_ADDR', '')[:255]
    path = request.META.get('PATH_INFO', '<unknown>')[:255]
    accept = request.META.get('HTTP_ACCEPT', '<unknown>')[:255]
    ua = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255]
    time = datetime.now()
    get = query2str(request.GET.items())
    post = query2str(request.POST.items())
    
    if login_unsuccessful:
        print "BAD LOGIN"
        return False 
    else:
        print "GOOD LOGIN"
        user = request.user
        access = Access.objects.create(
           user = user.username,
           user_agent = ua,
           ip_address = ip,
           get_data = get,
           post_data = post, 
           http_accept = accept, 
           path_info = path, 
        )
        return True
