def test_delete_meme(post_endpoint, delete_endpoint, auth_headers):
    payload = {
        "text": "Meme for delete",
        "url": "https://example.com/delete-meme.jpg",
        "tags": ["test", "delete"],
        "info": {"author": "tester"}
    }
    post_endpoint.create_meme(payload, auth_headers)
    post_endpoint.check_response_code()
    post_endpoint.check_meme_id_is_received()
    delete_endpoint.delete_meme_by_id(post_endpoint.meme_id, auth_headers)
    delete_endpoint.check_response_code()


def test_negative_delete_meme(delete_endpoint, create_meme_for_test):
    headers = {
        "Authorization": "wrong token"
    }
    delete_endpoint.delete_meme_by_id(create_meme_for_test, headers)
    delete_endpoint.check_unauthorized_response_code()
