import pytest

from ads.serializers import AdDetailSerializer
from tests.factories import AdFactory

@pytest.mark.django_db
def test_can_get_ads_list(client):
    ads = AdFactory.create_batch(3)

    expected_response = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdDetailSerializer(ads, many=True).data
    }

    response = client.get("/ads/ad/")

    assert response.status_code == 200
    assert response.data == expected_response
