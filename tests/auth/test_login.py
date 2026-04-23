"""
Authentication flow tests.

Entry point: / (SSO redirect)
Coverage:
  - Login page is reachable
  - Authenticated user lands on dashboard
  - Unauthenticated user is redirected to login
"""

import pytest
from faker import Faker
from playwright.sync_api import expect

from kamma_suite_regression.pages.login_page import LoginPage
from kamma_suite_regression.pages.dashboard_page import DashboardPage

fake = Faker()


@pytest.mark.smoke
@pytest.mark.auth
def test_login_page_is_reachable(page, base_url):
    """Verify the root URL loads without error and triggers the SSO flow."""
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.assert_page_loaded()


@pytest.mark.smoke
@pytest.mark.auth
def test_authenticated_user_reaches_dashboard(authenticated_page):
    """Verify that a session with valid auth state lands on the dashboard."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.assert_page_loaded()


@pytest.mark.regression
@pytest.mark.auth
def test_unauthenticated_user_redirected_to_login(page, base_url):
    """Verify that accessing a protected route without auth redirects to login."""
    page.goto(f"{base_url}/dashboard")
    # After redirect the URL should no longer be the dashboard
    expect(page).not_to_have_url(f"{base_url}/dashboard")


@pytest.mark.regression
@pytest.mark.auth
def test_invalid_credentials_shows_error(page):
    """Verify that submitting random credentials shows a login error."""
    login_page = LoginPage(page)
    login_page.login_with_invalid_credentials(
        email=fake.email(),
        password=fake.password(),
    )
    error = login_page.get_error_message()
    assert error == "These credentials do not match our records."
