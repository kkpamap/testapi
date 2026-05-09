import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    @allure.step("Update meme")
    def update_meme(self, meme_id, payload, headers):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=payload,
            headers=headers
            )
