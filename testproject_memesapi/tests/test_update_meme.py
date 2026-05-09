import pytest


def test_update_meme(put_endpoint, create_meme_for_test, auth_headers):
    payload = {
        "id": create_meme_for_test,
        "text": "Updated meme",
        "url": "https://example.com/updated-meme.jpg",
        "tags": ["updated", "api"],
        "info": {"author": "memecreator", "status": "updated"}
    }
    put_endpoint.update_meme(create_meme_for_test, payload, auth_headers)
    put_endpoint.check_response_code()
    put_endpoint.parse_response_json()
    put_endpoint.check_meme_data_is_correct(payload)


def test_negative_wrongtoken_update_meme(put_endpoint, create_meme_for_test):
    payload = {
        "id": create_meme_for_test,
        "text": "Updated meme",
        "url": "https://example.com/updated-meme.jpg",
        "tags": ["updated", "api"],
        "info": {"author": "memecreator"}
    }
    headers = {"Authorization": "wrong_token"}
    put_endpoint.update_meme(create_meme_for_test, payload, headers)
    put_endpoint.check_unauthorized_response_code()


@pytest.mark.parametrize(
    "payload",
    [
        {
            "text": "Updated meme",
            "url": "https://example.com/updated-meme.jpg",
            "tags": ["updated"],
            "info": {"author": "memecreator"}
        },
        {
            "id": 1,
            "url": "https://example.com/updated-meme.jpg",
            "tags": ["updated"],
            "info": {"author": "memecreator"}
        },
        {
            "id": 1,
            "text": "Updated meme",
            "tags": ["updated"],
            "info": {"author": "memecreator"}
        },
        {
            "id": 1,
            "text": "Updated meme",
            "url": "https://example.com/updated-meme.jpg",
            "info": {"author": "memecreator"}
        },
        {
            "id": 1,
            "text": "Updated meme",
            "url": "https://example.com/updated-meme.jpg",
            "tags": ["updated"]
        },
    ]
)
def test_negative_without_required_field_update_meme(put_endpoint, create_meme_for_test, auth_headers, payload):
    put_endpoint.update_meme(create_meme_for_test, payload, auth_headers)
    put_endpoint.check_bad_response_code()
