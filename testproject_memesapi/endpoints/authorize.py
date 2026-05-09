import allure
import requests

from endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    @allure.step("Authorize user")
    def authorize_user(self, name):
        self.response = requests.post(
            f"{self.url}/authorize",
            json={"name": name}
        )
        self.json = self.response.json()
        self.token = self.json.get("token")

    @allure.step("Check token is alive")
    def check_token_is_alive(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )

    @allure.step("Check token is received")
    def check_token_is_received(self):
        assert self.token is not None, 'Token is None'
