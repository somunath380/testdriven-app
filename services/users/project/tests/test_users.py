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

if __name__ == "__main__":
    unittest.main()



