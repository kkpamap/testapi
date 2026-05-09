import os
import pytest

from endpoints.authorize import Authorize
from endpoints.get_meme import GetMeme
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


TOKEN_FILE = "token.txt"


@pytest.fixture()
def authorize_endpoint():
    return Authorize()


@pytest.fixture(scope="session")
def token():
    authorize = Authorize()

    # если файл существует, проверяем старый токен
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as file:
            saved_token = file.read().strip()
        authorize.check_token_is_alive(saved_token)
        if authorize.response.status_code == 200:
            return saved_token

    # если файла нет или токен невалидный, то создаем новый
    authorize.authorize_user("memecreator")
    authorize.check_response_code()
    authorize.check_token_is_received()

    with open(TOKEN_FILE, "w", encoding="utf-8") as file:
        file.write(authorize.token)
    return authorize.token


@pytest.fixture(scope="session")
def auth_headers(token):
    return {"Authorization": token}


@pytest.fixture()
def get_endpoint():
    return GetMeme()


@pytest.fixture()
def post_endpoint():
    return CreateMeme()


@pytest.fixture()
def put_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_endpoint():
    return DeleteMeme()


@pytest.fixture()
def create_meme_for_test(post_endpoint, delete_endpoint, auth_headers):
    payload = {
        "text": "Created for test",
        "url": "https://example.com/meme.jpg",
        "tags": ["test"],
        "info": {"author": "tester"}
    }
    post_endpoint.create_meme(payload, auth_headers)
    post_endpoint.check_response_code()
    post_endpoint.check_meme_id_is_received()

    meme_id = post_endpoint.meme_id
    yield meme_id
    delete_endpoint.delete_meme_by_id(meme_id, auth_headers)
