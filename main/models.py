from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.


# Do not touch. This is custom user manager
# -----------------------------------------------------------------------

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    """Define a model manager for User model with no username field."""

    def _create_user(self, username, password=None, **extra_fields):
        """Create and save a User with the given mobile and password."""
        if not username:
            raise ValueError('The given username must be set')
        self.username = username
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given mobile and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


# --------------------------------------------------------------------------

class CustomUser(AbstractUser):
    username = models.CharField(_('user name'), unique=True, max_length=30)
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    date_created = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username + ' : ' + str(self.user_type)


# Below are all the masters. Zone,Depot,State,Cities
# _________________________________________________________

class Zone(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Depot(models.Model):
    name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    depot = models.ForeignKey(Depot, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + self.state.name
