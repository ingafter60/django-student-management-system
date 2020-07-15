from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_student.models import CustomUser

class UserModel(UserAdmin):
	pass

admin.site.register(CustomUser, UserModel)	