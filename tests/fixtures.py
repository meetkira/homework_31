from datetime import date

import pytest

from info.views import random_email
from users.models import User


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "admin"
    password = "test_password"
    role = User.ADMIN

    django_user_model.objects.create_user(username=username, password=password, first_name="test", role=role,
                                          birth_date=date(year=2000, month=1, day=1), email=random_email())

    response = client.post(
        "/users/token/",
        {"username": "admin", "password": "test_password"},
        format="json",
    )

    return response.data["access"]
