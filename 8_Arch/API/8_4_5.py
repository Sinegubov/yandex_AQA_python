class TestGithubApi:
    BASE_URL = 'https://api.github.com'
    TOKEN = '<имя твоего токена>'
    TEST_REPO_NAME = 'Hello-World'
    USERNAME = '<твой профиль на github - никнейм>'

    # хэдеры для методов POST, PATCH, DELETE
    self.headers = {
        'Authorization': f'Bearer {self.TOKEN}',
        'Accept': 'application/vnd.github+json'
    }
    # флаг — запускать teardown или нет
    self.run_teardown = True

    if self.run_teardown:
        ...  # тут будет тело метода