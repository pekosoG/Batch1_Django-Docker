from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _createUser(self, email, password, **extra_fields):
        if not email and not password:
            raise ValueError('Nooope, missing email/password field')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def createUser(self,email,password,**extra_field):
        return self._createUser(email,password,**extra_field)

class User(AbstractBaseUser):
    email = models.CharField(unique=True,max_length=50)
    objects = UserManager()
    USERNAME_FIELD = 'email'