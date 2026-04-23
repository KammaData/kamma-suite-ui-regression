import pytest
from kamma_suite_regression.fixtures.auth_fixtures import auth_storage_state  # noqa: F401
from kamma_suite_regression.request_utility.api_v3_request_utility import ApiV3RequestUtility


@pytest.fixture
def authenticated_page(browser, base_url, auth_storage_state):
    """
    Yields a Playwright Page pre-loaded with the authenticated session.
    Each test gets a fresh browser context (isolated cookies/storage) but
    inherits the saved login state so no re-login is needed.
    """
    context = browser.new_context(base_url=base_url, storage_state=auth_storage_state)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def api_v3():
    """Token-based API v3 client. Requires KAMMA_APIV3_TOKEN and KAMMA_APIV3_GROUP_ID in .env."""
    return ApiV3RequestUtility()


@pytest.fixture
def authenticated_request(playwright, base_url, auth_storage_state):
    """
    Yields a Playwright APIRequestContext authenticated via stored session.
    Use this alongside authenticated_page to fetch API data and compare it
    against what is rendered in the browser.
    """
    context = playwright.request.new_context(
        base_url=base_url,
        storage_state=auth_storage_state,
    )
    yield context
    context.dispose()
