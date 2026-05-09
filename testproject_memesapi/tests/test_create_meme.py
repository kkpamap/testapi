import pytest


def test_create_meme(post_endpoint, auth_headers):
    payload = {
        "text": "Test meme",
        "url": "https://i.pinimg.com/474x/aa/db/10/aadb10914ab1b0599dffa837cbb8f58b.jpg",
        "tags": ["dog", "fire"],
        "info": {"author": "memecreator", "color": "yellow"}
    }
    post_endpoint.create_meme(payload, auth_headers)
    post_endpoint.check_response_code()
    post_endpoint.check_meme_id_is_received()
    post_endpoint.parse_response_json()
    post_endpoint.check_meme_data_is_correct(payload)


@pytest.mark.parametrize(
    "payload",
    [
        {
            "text": "Test meme with wrong tags",
            "url": "https://example.com/meme.jpg",
            "tags": "test",
            "info": {"author": "memecreator"}
        },
        {
            "text": "Test meme with wrong info",
            "url": "https://example.com/meme.jpg",
            "tags": ["test", "api"],
            "info": "meme info"
        },
        {
            "text": "Test meme with wrong tags and info",
            "url": "https://example.com/meme.jpg",
            "tags": "test",
            "info": "meme info"
        },
    ]
)
def test_negative_create_meme(post_endpoint, payload, auth_headers):
    post_endpoint.create_meme(payload, auth_headers)
    post_endpoint.check_bad_response_code()


def test_negative_wrongtoken_create_meme(post_endpoint):
    payload = {
        "text": "Test meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["test"],
        "info": {"author": "memecreator"}
    }

    headers = {
        "Authorization": "wrong_token"
    }
    post_endpoint.create_meme(payload, headers)
    post_endpoint.check_unauthorized_response_code()
