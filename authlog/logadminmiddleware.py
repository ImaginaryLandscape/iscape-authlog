from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.admin import site
# from django.contrib.admin.sites import ModelAdmin
from django.contrib.admin.options import ModelAdmin
from authlog.decorators import watch_login, watch_view

# watch admin views; Move outsite the function because Django create admin objects during initiating
ModelAdmin.change_view = watch_view(ModelAdmin.change_view)
ModelAdmin.changelist_view = watch_view(ModelAdmin.changelist_view)
ModelAdmin.add_view = watch_view(ModelAdmin.add_view)
ModelAdmin.delete_view = watch_view(ModelAdmin.delete_view)

class LogAdminMiddleware(object):

    def process_request(self, request):
        auth_views.login = watch_login(auth_views.login)
        #Admin now uses site.login for handling admin login request
        site.login = watch_login(site.login)
