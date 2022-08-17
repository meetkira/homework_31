from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
from users.validators import check_email_validator, check_age_validator


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Расположение"
        verbose_name_plural = "Расположения"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"

    ROLE = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    role = models.CharField(max_length=9, default="member", choices=ROLE)
    #age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_age_validator])
    email = models.EmailField(unique=True, validators=[check_email_validator])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
