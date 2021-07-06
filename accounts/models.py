from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator
from datetime import datetime


phone_regex = RegexValidator("^0\d{8,10}$", "your phone number is not valid")

SEX = (
	('Male', 'Male'),
	('Female', 'Female')
	)

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("must have email")
		if not username:
			raise ValueError("must have username")

		user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

		user.set_password(password)
		user.save(using=self._db)
		return user			

	def create_superuser(self, email, username, password=None):
		user = self.create_user(email=self.normalize_email(email), username=username, password=password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True

		user.save(using=self._db)
		return user

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
	username = models.CharField(max_length=50, default="user")
	sex = models.CharField(max_length=10, verbose_name="Sex", choices=SEX, default="Female")
	phone_num = models.CharField(max_length=10, verbose_name="Phone number", validators=[phone_regex], null=True, unique=True)

	date_joined = models.DateTimeField (verbose_name="date joined", default=datetime.now())
	last_login = models.DateTimeField (verbose_name="last login", default=datetime.now())
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', ]

	object = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
	    return True