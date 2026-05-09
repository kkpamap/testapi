def test_authorize(authorize_endpoint):
    authorize_endpoint.authorize_user('qamemecreator')
    authorize_endpoint.check_response_code()
    authorize_endpoint.check_token_is_received()
