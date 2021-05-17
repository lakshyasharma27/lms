from django.contrib.auth.models import BaseUserManager
from .choiceTypes import UserType
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a User with the given email and password.
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_("User should have an email"))
        if not password:
            raise ValueError(_("User should have an password"))
        if not user_name:
            raise ValueError(_("User should have an user_name"))
        if not first_name:
            raise ValueError(_("User should have an first_name"))

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name, first_name=first_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('user_type', UserType.admin)

        if other_fields.get('is_staff') is not True:
            raise ValueError("SuperUser must be assigned to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "SuperUser must be assigned to is_superuser=True.")
        if other_fields.get('is_active') is not True:
            raise ValueError(
                "SuperUser must be assigned to is_active=True.")
        if other_fields.get('user_type') is None:
            raise ValueError(
                "SuperUser must be assigned to user_type=admin.")

        return self.create_user(email=email, password=password, user_name=user_name, first_name=first_name, **other_fields)


class HODManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a User with the given email and password.
        """
        other_fields.setdefault('user_type', UserType.hod)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_("User should have an email"))
        if not password:
            raise ValueError(_("User should have an password"))
        if not user_name:
            raise ValueError(_("User should have an user_name"))
        if not first_name:
            raise ValueError(_("User should have an first_name"))
        if other_fields.get('is_staff') is not True:
            raise ValueError("User must be assigned to is_staff=True.")
        if other_fields.get('is_active') is not True:
            raise ValueError(
                "User must be assigned to is_active=True.")
        if other_fields.get('user_type') is None:
            raise ValueError(
                "User must be assigned to user_type=hod.")

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name, first_name=first_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class ProfessorManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Creates and saves a User with the given email and password.
        """
        # print(other_fields.pop("password2"))
        other_fields.setdefault('user_type', UserType.professor)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_("User should have an email"))
        if not password:
            raise ValueError(_("User should have an password"))
        if not user_name:
            raise ValueError(_("User should have an user_name"))
        if not first_name:
            raise ValueError(_("User should have an first_name"))
        if other_fields.get('is_staff') is not True:
            raise ValueError("User must be assigned to is_staff=True.")
        if other_fields.get('is_active') is not True:
            raise ValueError(
                "User must be assigned to is_active=True.")
        if other_fields.get('user_type') is None:
            raise ValueError(
                "User must be assigned to user_type=hod.")

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name, first_name=first_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_professors_based_on_user(self, user):
        if user.is_admin() is True:
            return super().get_queryset().all()
        else:
            return super().get_queryset().filter(
                department=user.HODs.department)
