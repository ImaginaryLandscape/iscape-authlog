from __future__ import absolute_import
from authlog.decorators import watch_login, watch_view
from django.contrib import admin
from django.contrib.admin import site
# from django.contrib.admin.sites import ModelAdmin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth import views as auth_views

# watch admin views; Move outsite the function because Django create admin objects during initiating
ModelAdmin.change_view = watch_view(ModelAdmin.change_view)
ModelAdmin.changelist_view = watch_view(ModelAdmin.changelist_view)
ModelAdmin.add_view = watch_view(ModelAdmin.add_view)
ModelAdmin.delete_view = watch_view(ModelAdmin.delete_view)

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class LogAdminMiddleware(MiddlewareMixin):

    def process_request(self, request):
        auth_views.LoginView = watch_login(auth_views.LoginView)
        #Admin now uses site.login for handling admin login request
        site.login = watch_login(site.login)
