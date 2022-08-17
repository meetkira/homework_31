import pytest


@pytest.mark.django_db
def test_can_get_ad(client, ad, user_token):

    expected_response = {
        "id": ad.pk,
        "category": "test category",
        "author": "test first_name",
        "name": "test ad 10",
        "price": 100,
        "description": "test description",
        "is_published": False,
        "image": None
    }

    response = client.get(f"/ads/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.status_code == 200
    assert response.data == expected_response
