from playwright.sync_api import Page, expect
from kamma_suite_regression.pages.base_page import BasePage


class ExportPage(BasePage):
    PATH = "/exports"

    def __init__(self, page: Page):
        super().__init__(page)
        self.export_button = page.locator("button:has-text('Export Portfolio')")

    def navigate(self):
        super().navigate(self.PATH)
        self.wait_for_network_idle()

    def assert_page_loaded(self):
        expect(self.export_button).to_be_visible()
