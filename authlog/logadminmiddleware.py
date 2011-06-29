from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.admin.sites import ModelAdmin
from authlog.decorators import watch_login, watch_view

class LogAdminMiddleware(object):

    def process_request(self, request):
        # and the regular auth login page
        auth_views.login = watch_login(auth_views.login)

        ModelAdmin.change_view = watch_view(ModelAdmin.change_view,)
        ModelAdmin.changelist_view = watch_view(ModelAdmin.changelist_view,)
        ModelAdmin.add_view = watch_view(ModelAdmin.add_view,)
        ModelAdmin.delete_view = watch_view(ModelAdmin.delete_view,)
