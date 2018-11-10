import unittest
import json

from run import create_app
from api.models.models import Parcel, parcel_orders


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()
        self.parcel_orders = parcel_orders

    def test_create_order(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="meru", parcel_weight=48,
                          parcel_description="apples", status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert "message" in str(response.data)






