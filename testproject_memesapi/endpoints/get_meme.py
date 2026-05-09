import allure
import requests
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.step("Get all memes")
    def get_all_memes(self, headers):
        self.response = requests.get(
            f"{self.url}/meme",
            headers=headers
            )
        self.json = self.response.json()
        return self.response

    @allure.step("Check memes list is not empty")
    def check_memes_not_empty(self):
        assert len(self.json) > 0, 'Memes list is empty'

    @allure.step("Get meme by id")
    def get_meme_by_id(self, meme_id, headers):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers=headers
            )
        self.json = self.response.json()
        return self.response

    @allure.step("Check we got one meme")
    def check_got_one_meme(self):
        assert isinstance(self.json, dict), 'Got not only one meme'

    @allure.step("Check meme has all fields")
    def check_meme_has_required_fields(self):
        assert self.json.get("id") is not None, "Meme id is missing"
        assert self.json.get("text"), "Meme text is missing"
        assert self.json.get("url"), "Meme url is missing"
        assert self.json.get("tags"), "Meme tags are missing"
        assert self.json.get("info"), "Meme info is missing"
