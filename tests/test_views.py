import unittest
import json

from run import create_app
from api.models.models import Parcel


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()
        self.parcel_orders = Parcel.parcel_orders

    def test_data_structure(self):
        self.assertTrue(isinstance(Parcel.parcel_orders, list))

    def test_create_order(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="meru", parcel_weight=48,
                          parcel_description="apples", user_id=1, status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "message" in str(response.data)
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"

    def test_empty_parcel_location_fields(self):
        post_order = dict(parcel_location=" ", parcel_destination="meru", parcel_weight=48,
                          parcel_description="apples",user_id=1,  status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "parcel location can not be parced empty string" in json.loads(response.data)['error']['parcel_location']

    def test_empty_parcel_destination_fields(self):
        post_order = dict(parcel_location="kisumu", parcel_destination=" ", parcel_weight=48,
                          parcel_description="apples",user_id=1, status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "parcel destination can not be parced empty string" in json.loads(response.data)['error']['parcel_destination']

    def test_empty_parcel_weight_fields(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="mbale", parcel_weight= -1,
                          parcel_description="apples", user_id=1, status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "weight cant be less than " in json.loads(response.data)['error']['parcel_weight']

    def test_empty_parcel_description_fields(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="mbale", parcel_weight= 78,
                          parcel_description=" ",user_id=1, status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "parcel description can not be parced empty string" in json.loads(response.data)['error']['parcel_description']

    def test_empty_status_fields(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="mbale", parcel_weight=78,
                          parcel_description="apples", user_id=1, status=" ")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "parcel status can not be parcel empty string" in json.loads(response.data)['error']['status']

    def test_user_id_fields(self):
        post_order = dict(parcel_location="kisumu", parcel_destination="mbale", parcel_weight=78,
                          parcel_description="apples", user_id=-1, status="pending")
        response = self.app.post('/api/v1/parcel', json=post_order)
        assert "error" in str(response.data)
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert "user_id cant be less than 0" in json.loads(response.data)['error']['user_id']

    def test_get_all_parcels(self):
        post_order = dict(parcel_location="jinja", parcel_destination="manafwa", parcel_weight=24.7,
                          parcel_description="apples", user_id=1, status="pending")
        post_order2 = dict(parcel_location="kisumu", parcel_destination="mbale", parcel_weight=78,
                           parcel_description="eggs", user_id=2, status="cancelled")
        response = self.app.post('/api/v1/parcel', json=post_order)
        response2 = self.app.post('/api/v1/parcel', json=post_order2)
        response3 = self.app.get('/api/v1/parcel')
        assert response3.status_code == 200
        assert response3.headers["Content-Type"] == "application/json"
        assert "jinja" and "kisumu" in str(response3.data)

    def test_get_parcel_by_id(self):
        response = self.app.post('/api/v1/parcel')
        response1 = self.app.get('/api/v1/parcel/1')
        response2 = self.app.get('api/v1/parcel/w')
        assert response1.status_code == 200
        assert response2.status_code == 404
        assert response1.headers["Content-Type"] == "application/json"













