from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import HODManager, ProfessorManager, UserManager
from .choiceTypes import UserType, DepartmentType


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"), unique=True, db_index=True)
    user_name = models.CharField(max_length=20, unique=True, db_index=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=10, choices=UserType.choices, default=UserType.professor)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    objects = UserManager()

    def __str__(self):
        return self.user_name

    def get_fullname(self):
        return self.first_name+" "+self.last_name

    def get_shortname(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_hod(self):
        return self.user_type == UserType.hod

    def is_professor(self):
        return self.user_type == UserType.professor

    def is_admin(self):
        return self.user_type == UserType.admin

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class HOD(User):
    date_of_joining = models.DateField()
    department = models.CharField(
        max_length=20, choices=DepartmentType.choices)
    degree = models.CharField(max_length=20)

    objects = HODManager()

    class Meta:
        default_related_name = "HODs"
        verbose_name_plural = "HODs"
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_invalid_department_type",
                check=models.Q(department__in=DepartmentType.values),
            )
        ]


class Professor(User):
    date_of_joining = models.DateField()
    department = models.CharField(
        max_length=20, choices=DepartmentType.choices)
    degree = models.CharField(max_length=20)

    objects = ProfessorManager()

    class Meta:
        default_related_name = "Professors"
        verbose_name_plural = "Professors"
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_invalid_department_type",
                check=models.Q(department__in=DepartmentType.values),
            )
        ]
