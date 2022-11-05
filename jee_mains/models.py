from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password):

        if not email:
            raise ValueError("Users must have an email address.")

        if not password:
            raise ValueError("Users must provide a password")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, name, password):

        user = self.create_user(
            email=email,
            password=password,
            name=name,
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email=email, password=password, name=name)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, verbose_name="Name")
    lname = models.CharField(max_length=255, verbose_name="Last Name")
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    tc_accept = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    analytics_sent = models.BooleanField(default=False)
    last_subscription_updated = JSONField()

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email

    @property
    def isactive(self):
        return self.is_active

    @property
    def isstaff(self):
        return self.is_staff

    @property
    def issuperuser(self):
        return self.is_superuser



class jee_mains(models.Model): 
    # url   = models.CharField(max_length=1000, default="", null=True)
    url   = models.SlugField(max_length=1000, default="", null=True)
    year  = models.IntegerField(null=True) 
    date  = models.IntegerField(null=True)
    # month  = models.IntegerField()
    month  = models.CharField(max_length=100, default="", null=True)
    shift  = models.CharField(max_length=100, default="", null=True)
    question = models.TextField()
    options = ArrayField(models.CharField(max_length=5000, default=[]))
    subject  = models.CharField(max_length=100, default="", null=True)
    question_images = ArrayField(models.CharField(max_length=5000, default=[],  null=True))
    solution_images = ArrayField(models.CharField(max_length=5000, default=[], null=True))
    option_images = ArrayField(models.CharField(max_length=5000, default=[] , null=True))
    correct_option = models.CharField(max_length=100, default="", null=True)
    solution = models.TextField()
    times_loaded = models.CharField(max_length=1000, default="", null=True)
    def get_absolute_url(self):
        return reverse("jee_mains_single", kwargs={"url": self.url})

class TestSeriesMap(models.Model):
    physics_ques_map = ArrayField(models.IntegerField(default=[]))
    chemistry_ques_map = ArrayField(models.IntegerField( default=[]))
    maths_ques_map = ArrayField(models.IntegerField(default=[]))
