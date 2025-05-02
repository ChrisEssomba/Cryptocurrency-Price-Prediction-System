'''
This file sets up fixtures (reusable test components) for pytest.
Fixture 1: app()

    Provides a Flask app instance in testing mode (TESTING=True).

    Ensures the app is properly configured for tests (e.g., no debug mode interference).

Fixture 2: client(app)

    Provides a test HTTP client for making requests to the Flask app.

    Used in integration tests to simulate browser requests.

Why is this important?

    Avoids code duplication by centralizing test setup.

    Ensures all tests use the same app configuration.
'''
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()