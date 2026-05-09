import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step("Delete meme by id")
    def delete_meme_by_id(self, meme_id, headers):
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=headers,
        )
        return self.response
