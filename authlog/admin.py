from django.contrib import admin
from authlog.models import Access, AccessPage

from django import forms

class ReadOnlyWidget(forms.Widget):
    def __init__(self, original_value, display_value):
        self.original_value = original_value
        self.display_value = display_value

        super(ReadOnlyWidget, self).__init__()

    def render(self, name, value, attrs=None):
        if self.display_value is not None:
            return unicode(self.display_value)
        return unicode(self.original_value)

    def value_from_datadict(self, data, files, name):
        return self.original_value

class ReadOnlyAdminFields(object):
    def get_form(self, request, obj=None):
        form = super(ReadOnlyAdminFields, self).get_form(request, obj)

        if hasattr(self, 'readonly'):
            for field_name in self.readonly:
                if field_name in form.base_fields:

                    if hasattr(obj, 'get_%s_display' % field_name):
                        display_value = getattr(obj, 'get_%s_display' % field_name)()
                    else:
                        display_value = None

                    form.base_fields[field_name].widget = ReadOnlyWidget(getattr(obj, field_name, ''), display_value)
                    form.base_fields[field_name].required = False

        return form



class AccessAdmin(ReadOnlyAdminFields, admin.ModelAdmin):
    list_display = ('user','login_time', 'ip_address', 'ip_forward', 'get_path_info_link', )
    list_filter = ['user','login_time', 'ip_address', ]
    search_fields = ['user','ip_address', 'user_agent', 'path_info']
    date_hierarchy = 'login_time'
    readonly = ['user','ip_address', 'ip_forward', 'user_agent', 'path_info','get_data','post_data','http_accept',]
    fieldsets = (
        (None, {
            'fields': ('user','path_info',)
        }),
        ('Form Data', {
            'fields': ('get_data', 'post_data')
        }),
        ('Meta Data', {
            'fields': ('user_agent', 'ip_address', 'ip_forward', 'http_accept')
        })
    )

    def get_actions(self, request):
        return None
 
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_path_info_link(self, obj):
        return '<a href="%s%s">%s</a>' % ('', obj.path_info, obj.path_info)
    get_path_info_link.allow_tags = True
    get_path_info_link.short_description = 'Path'


class AccessPageAdmin(ReadOnlyAdminFields, admin.ModelAdmin):
    list_display = ('user','access_time', 'ip_address', 'ip_forward', 'get_path_info_link','action_type', )
    list_filter = ['user','access_time', 'ip_address', 'action_type',]
    search_fields = ['user','ip_address', 'ip_forward', 'user_agent', 'path_info']
    date_hierarchy = 'access_time'
    readonly = ['user','ip_address', 'ip_forward', 'user_agent',
                'path_info','get_data','post_data','http_accept','action_type']
    fieldsets = (
        (None, {
            'fields': ('user','path_info','action_type',)
        }),
        ('Form Data', {
            'fields': ('get_data', 'post_data')
        }),
        ('Meta Data', {
            'fields': ('user_agent', 'ip_address', 'ip_forward', 'http_accept')
        })
    )

    def get_actions(self, request):
        return None
 
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_path_info_link(self, obj):
        return '<a href="%s%s">%s</a>' % ('', obj.path_info, obj.path_info)
    get_path_info_link.allow_tags = True
    get_path_info_link.short_description = 'Path'


admin.site.register(Access, AccessAdmin)
admin.site.register(AccessPage, AccessPageAdmin)
