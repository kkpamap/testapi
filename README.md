# Memes API Tests

Project for API testing of http://memesapi.course.qa-practice.com/

## Project structure

### endpoints/
Contains classes for API endpoints:
- authorize.py
- create_meme.py
- get_meme.py
- update_meme.py
- delete_meme.py

All endpoint classes inherit from `Endpoint` base class.

### tests/
Contains API tests grouped by endpoints:
- authorization tests
- create meme tests
- get meme tests
- update meme tests
- delete meme tests

### conftest.py
Contains pytest fixtures:
- authorization token
- authorization headers
- endpoint objects
- fixtures for test meme creation and cleanup
