from django.db import models

class Access(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.IPAddressField('IP Address', blank=True, null=True)
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
    ip_address = models.IPAddressField('IP Address', blank=True, null=True)
    get_data = models.TextField('GET Data', blank=True, null=True)
    post_data = models.TextField('POST Data', blank=True, null=True)
    http_accept = models.CharField('HTTP Accept', max_length=255, blank=True, null=True)
    path_info = models.CharField('Path', max_length=255, blank=True, null=True)
    access_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Access: %s at %s by %s' % (self.access_time, self.ip_address, self.user)

    class Meta:
        ordering = ['-access_time']
        verbose_name = "Page Access"
        verbose_name_plural = "Page Accesses"


