from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "date_joined", "last_login", "is_staff", "is_admin")
	search_fields = ("email", "username", )
	readonly_fields = ("date_joined", "last_login")

	filter_horizontal = ("groups", "user_permissions", )
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)