from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Options


class RestrictedUserAdmin(UserAdmin):
    """
    Prevent permission escalation in when granting “user change” permissions
    See: http://stackoverflow.com/a/2298268
    """
    staff_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        # No permissions
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    )

    def change_view(self, request, *args, **kwargs):
        # for non-superuser
        if not request.user.is_superuser:
            try:
                self.fieldsets = self.staff_fieldsets
                response = UserAdmin.change_view(self, request, *args, **kwargs)
            finally:
                # Reset fieldsets to its original value
                self.fieldsets = UserAdmin.fieldsets
            return response
        else:
            return UserAdmin.change_view(self, request, *args, **kwargs)

admin.site.unregister(User)
admin.site.register(User, RestrictedUserAdmin)


class OptionsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """
        Don't allow addition of 2nd model instance in Django admin
        See: http://stackoverflow.com/a/12469482
        """
        if self.model.objects.count() > 0:
            return False
        else:
            return True

admin.site.register(Options, OptionsAdmin)
