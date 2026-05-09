import allure
import requests
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step("Create meme")
    def create_meme(self, payload, headers):
        self.response = requests.post(
            f"{self.url}/meme",
            json=payload,
            headers=headers
            )

    @allure.step("Check meme id is received")
    def check_meme_id_is_received(self):
        self.meme_id = self.response.json().get("id")
        assert self.meme_id is not None, 'Meme id is not received'
