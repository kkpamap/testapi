def test_get_all_memes(get_endpoint, auth_headers):
    get_endpoint.get_all_memes(auth_headers)
    get_endpoint.check_response_code()
    get_endpoint.check_memes_not_empty()


def test_get_meme_by_id(get_endpoint, create_meme_for_test, auth_headers):
    get_endpoint.get_meme_by_id(create_meme_for_test, auth_headers)
    get_endpoint.check_response_code()
    get_endpoint.check_got_one_meme()
    get_endpoint.check_meme_has_required_fields()
