from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "date_joined", "last_login", "is_staff", "is_admin")
	search_fields = ("email", "username", )
	readonly_fields = ("date_joined", "last_login")

	filter_horizontal = ("groups", )
	list_filter = ("groups", "is_active")
	fieldsets = ()

	fieldsets = (
        ('Personal Information', {'fields': ('email', 'username', 'sex', 'phone_num')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin')}),
		('Roles', {'fields':('groups',)}),
    )
	# formfield_overrides = {
    #     Account.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_num', 'sex', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin')}
         ),
    )

admin.site.register(Account, AccountAdmin)