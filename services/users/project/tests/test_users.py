import json
import unittest
from project.tests.base import BaseTestCase
class TestUserService(BaseTestCase):
    def test_users(self):
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert "pong!" in data["message"]
        assert "success" in data["status"]

    def test_add_user(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'somu',
                    'email': 'somunath@gmail.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assert200(response)
            assert 'somunath@gmail.com was added!' in data['message']
            assert 'success' in data['status']
    
    def test_add_user_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            assert 'Invalid payload.' in data['message']
            assert 'fail' in data['status']

    def test_add_user_invalid_json_keys(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'somunath@gmail.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            assert 'Invalid payload.' in data['message']
            assert 'fail' in data['status']
    
    def test_add_user_duplicate_email(self):
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'somunath',
                    'email': 'somunath@gmail.com'
                }),
                content_type='application/json'
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'somunath',
                    'email': 'somunath@gmail.com'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assert400(response)
            assert 'Sorry! That email already exists.' in data['message']
            assert 'fail' in data['status']
    

if __name__ == "__main__":
    unittest.main()



