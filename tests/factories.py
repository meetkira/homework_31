from datetime import date

import factory.django

from ads.models import Category, Ad
from info.views import random_email, random_lower_string
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test category"
    slug = factory.Faker("password", length=7)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "test"
    role = User.ADMIN
    first_name = "test first_name"
    birth_date = date(year=2000, month=1, day=1)
    email = factory.Faker("email")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test ad 10"
    price = 100
    description = "test description"
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
