from django.db import models


class UserType(models.TextChoices):
    hod = "HOD"
    admin = "Admin"
    professor = "Professor"


class DepartmentType(models.TextChoices):
    cse = "Computer Science"
    mechanical = "Mechanical"
    electronics = "Electronics"
    electrical = "Electrical"
