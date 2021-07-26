from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, name, password=None):
        """Create a new user"""

        if not email:
            raise ValueError('Users must have an email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def __str__(self):
        """Return string reprensation of our users"""
        return self.email


class Band(models.Model):
    """Database models for satellit's bands information"""

    band = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    in_satellite = models.ForeignKey('Satellite', on_delete=models.PROTECT, blank=True, null=True)
    wavelength = models.DecimalField(max_digits=4, decimal_places=0, default='0', help_text='Central wavelength (nm)')
    resolution = models.DecimalField(max_digits=4, decimal_places=0, default='0', help_text='Spatial resolution (m)')

    def __str__(self):
        return '%s | %s' % (self.in_satellite, self.band)


class Satellite(models.Model):
    """Database models for satellite information"""

    name = models.CharField(max_length=255)
    accr = models.CharField(max_length=3)
    task = models.CharField(max_length=256, choices=[('SAR', 'SAR'), ('MSI', 'MSI')])
    operator = models.CharField(max_length=255, default='European Space Agency')

    def __str__(self):
        return self.name


class Indice(models.Model):
    """Database models for index information"""

    name = models.CharField(max_length=255)
    accr = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    is_NormalizedDifference = models.BooleanField(blank=True, help_text='Is this indice a normalized difference?')
    calc = models.CharField(max_length=255, blank=True, help_text='Use calculation just for if normalized difference is checked!')
    satellite_to_use = models.ForeignKey('Satellite', on_delete=models.PROTECT, blank=True, null=True)
    needed_bands = models.ManyToManyField(Band)

    def __str__(self):
        return self.name


class Application(models.Model):
    """Database models for application information"""

    name = models.CharField(max_length=255)
    machine_name = models.SlugField(max_length=255, allow_unicode=True)
    description = models.TextField(blank=True, null=True)
    indice_to_use = models.ForeignKey('Indice', on_delete=models.PROTECT, blank=True, null=True)
    bands = models.CharField(max_length=200, default='B2, B3, B4')

    def get_bands(self):
        return json.loads(self.bands)

    def __str__(self):
        return self.name
