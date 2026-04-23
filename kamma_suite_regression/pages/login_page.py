from playwright.sync_api import Page, expect
from kamma_suite_regression.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Handles the SSO login entry point.

    The actual login form is served by an SSO provider — update the locators
    below once the provider's form structure is confirmed. The pattern here
    assumes an email/password form; adjust if the provider uses a different flow
    (e.g., a redirect-only flow where credentials are entered on an external domain).
    """

    def __init__(self, page: Page):
        super().__init__(page)
        # TODO: update locators to match the actual SSO provider form
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Sign in")
        self.error_message = page.get_by_text("These credentials do not match our records.")

    def navigate_to_login(self):
        self.navigate("/")
        self.wait_for_network_idle()

    def login(self, email: str, password: str):
        """Automate the SSO login flow and wait for the post-login redirect."""
        self.navigate_to_login()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        # TODO: update the URL pattern to match the post-login destination
        self.page.wait_for_url("**/dashboard**", timeout=20_000)

    def login_with_invalid_credentials(self, email: str, password: str):
        """Submit invalid credentials and stay on the login page."""
        self.navigate_to_login()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def get_error_message(self) -> str:
        """Return the visible error message text after a failed login."""
        self.error_message.wait_for(state="visible", timeout=10_000)
        return self.error_message.inner_text()

    def assert_page_loaded(self):
        """Verify the login entry point is reachable (pre-auth landing page)."""
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).not_to_have_url("about:blank")
