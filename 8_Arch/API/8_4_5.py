import requests


class TestGithubApi:
    BASE_URL = "https://api.github.com"
    TOKEN = "........."
    TEST_REPO_NAME = "Hello-World"
    USERNAME = "Sinegubov"

    def setup_method(self):
        # хэдеры для методов POST, PATCH, DELETE
        self.headers = {
            "Authorization": f'Bearer {self.TOKEN}',
            "Accept": "application/vnd.github+json"
        }
        # флаг — запускать teardown или нет
        self.run_teardown = True

    def test_get_user(self):
        self.run_teardown = False
        response = requests.get(f"{self.BASE_URL}/users/{self.USERNAME}")

        assert response.status_code == 200
        assert response.json()["login"] == self.USERNAME

    def test_create_repo(self):
        self.run_teardown = False
        response = requests.post(f"{self.BASE_URL}/user/repos",
                                 json={
                                        "name": self.TEST_REPO_NAME,
                                        "description": "Тестовое описание",
                                        "private": False,
                                        "is_template": True
                                        }, headers=self.headers)

        assert response.status_code == 201
        assert response.json()["name"] == self.TEST_REPO_NAME

    def test_update_repo(self):
        self.run_teardown = True
        owner = self.USERNAME
        repo = self.TEST_REPO_NAME
        response = requests.patch(f"{self.BASE_URL}/repos/{owner}/{repo}",
                                  json={
                                        "description": "Новое описание"
                                        }, headers=self.headers)

        assert response.status_code == 200
        assert response.json()["description"] == "Новое описание"

    def teardown_method(self):
        if self.run_teardown:
            owner = self.USERNAME
            repo = self.TEST_REPO_NAME
            response = requests.delete(f"{self.BASE_URL}/repos/{owner}/{repo}", headers=self.headers)

            assert response.status_code == 204
