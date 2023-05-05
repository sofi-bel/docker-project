import requests

URL = "docker-projects-app-1:5000"


class TestIntegration:
    def test_files_return_code(self):
        response = requests.get(f"http://{URL}/files")
        assert response.status_code == 200

    def test_wrong_login_return_code(self):
        response = requests.post(
            f"http://{URL}/login", data={"name": "tests", "password": "1234test"}
        )
        assert response.status_code == 401
