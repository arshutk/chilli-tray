from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('users must have an username')

        if not password:
            raise ValueError('users must provide a password')

        user = self.model(
            username = username,
        )

        user.is_active = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Custom User models extending AbstractBaseUser class'''

    username = models.CharField(max_length=256, unique=True ,validators=[RegexValidator(regex='^[aA].*[01]$', 
                                message='username must start with a/A and ends with 0/1')])
    join_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = "User"

