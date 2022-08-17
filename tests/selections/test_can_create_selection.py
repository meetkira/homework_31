import pytest

from tests.factories import AdFactory

@pytest.mark.django_db
def test_can_create_selection(client, user_token):
    ads = AdFactory.create_batch(3)

    expected_response = {
        "id": 1,
        "name": "test selection",
        "owner": 1,
        "items": [ads[0].id, ads[1].id, ads[2].id],
    }

    data = {
        "name": "test selection",
        "owner": 1,
        "items": [ads[0].id, ads[1].id, ads[2].id],
    }

    response = client.post(
        "/selections/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
