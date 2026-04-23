import os
import pytest
from kamma_suite_regression.pages.login_page import LoginPage

AUTH_STATE_PATH = "test_data/auth_state.json"


@pytest.fixture(scope="session")
def auth_storage_state(browser, base_url):
    """
    Logs in once per test session and caches the browser storage state
    (cookies + localStorage) to AUTH_STATE_PATH.

    Subsequent fixture calls in the same session reuse the cached file,
    avoiding a login round-trip on every test. Delete auth_state.json to
    force a fresh login (e.g. after token expiry).
    """
    if os.path.exists(AUTH_STATE_PATH):
        return AUTH_STATE_PATH

    email = os.environ.get("SUITE_USERNAME", "")
    password = os.environ.get("SUITE_PASSWORD", "")

    if not email or not password:
        raise EnvironmentError(
            "SUITE_USERNAME and SUITE_PASSWORD must be set in your .env file "
            "before running tests that require authentication."
        )

    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.login(email=email, password=password)

    os.makedirs(os.path.dirname(AUTH_STATE_PATH), exist_ok=True)
    context.storage_state(path=AUTH_STATE_PATH)
    context.close()

    return AUTH_STATE_PATH
