import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    response = None
    json = None

    @allure.step("Check that response code is 200")
    def check_response_code(self):
        assert self.response.status_code == 200, 'Not 200 status code returned'

    @allure.step("Check that response code is 400")
    def check_bad_response_code(self):
        assert self.response.status_code == 400, 'Not 400 status code returned'

    @allure.step("Check that response code is 401")
    def check_unauthorized_response_code(self):
        assert self.response.status_code == 401, 'Not 401 status code returned'

    @allure.step("Parse response json")
    def parse_response_json(self):
        self.json = self.response.json()

    @allure.step("Check meme data is correct")
    def check_meme_data_is_correct(self, payload):
        assert self.json["text"] == payload["text"], 'Wrong meme text'
        assert self.json["url"] == payload["url"], 'Wrong meme url'
        assert self.json["tags"] == payload["tags"], 'Wrong meme tags'
        assert self.json["info"] == payload["info"], 'Wrong meme info'
