import pytest


@pytest.mark.django_db
def test_can_create_ad(client, user_token, category):

    expected_response = {
        "id": 1,
        "category": 1,
        "author": 1,
        "name": "test name 10",
        "price": 100,
        "description": "test",
    }

    data = {
        "category": category.id,
        "author": 1,
        "name": "test name 10",
        "price": 100,
        "description": "test",
    }

    response = client.post(
        "/ads/ad/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
