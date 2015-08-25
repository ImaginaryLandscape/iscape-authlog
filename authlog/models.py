from django.db import models
from collections import defaultdict

ACTION_TYPE = defaultdict(lambda: 0)  # return 0 if action not defined
ACTION_TYPE.update(dict(VIEW_CHANGE=1, SUBMIT_CHANGE=2, VIEW_DELETE=3,
                        SUBMIT_DELETE=4, VIEW_HISTORY=5, VIEW_LIST=6,
                        VIEW_ADD=7, SUBMIT_ADD=8, DOWNLOAD_CSV=9))

ACTION_TYPE_T = ((0, 'OTHER'), (1, 'VIEW_CHANGE'), (2, 'SUBMIT_CHANGE'), (3, 'VIEW_DELETE'),
                 (4, 'SUBMIT_DELETE'), (5, 'VIEW_HISTORY'), (6, 'VIEW_LIST'),
                 (7, 'VIEW_ADD'), (8, 'SUBMIT_ADD'), (9, 'DOWNLOAD_CSV'))


class Access(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField('IP Address', max_length=255, blank=True, null=True)
    ip_forward = models.CharField('IP Forward Address', max_length=255, blank=True, null=True)
    get_data = models.TextField('GET Data', blank=True, null=True)
    post_data = models.TextField('POST Data', blank=True, null=True)
    http_accept = models.CharField('HTTP Accept', max_length=255, blank=True, null=True)
    path_info = models.CharField('Path', max_length=255, blank=True, null=True)
    login_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Access: %s at %s' % (self.login_time, self.ip_address)

    class Meta:
        ordering = ['-login_time']
        verbose_name = "Login Access"
        verbose_name_plural = "Login Accesses"


class AccessPage(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField('IP Address', max_length=255, blank=True, null=True)
    ip_forward = models.CharField('IP Forward Address', max_length=255, blank=True, null=True)
    get_data = models.TextField('GET Data', blank=True, null=True)
    post_data = models.TextField('POST Data', blank=True, null=True)
    http_accept = models.CharField('HTTP Accept', max_length=255, blank=True, null=True)
    path_info = models.CharField('Path', max_length=255, blank=True, null=True)
    access_time = models.DateTimeField(auto_now_add=True)
    action_type = models.IntegerField(choices=ACTION_TYPE_T, blank=True, null=True)

    def __unicode__(self):
        return u'Access: %s at %s by %s' % (self.access_time, self.ip_address, self.user)

    class Meta:
        ordering = ['-access_time']
        verbose_name = "Page Access"
        verbose_name_plural = "Page Accesses"
