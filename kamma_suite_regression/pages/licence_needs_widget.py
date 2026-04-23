from playwright.sync_api import Page
from kamma_suite_regression.pages.base_page import BasePage


class LicenceNeedsWidget(BasePage):
    """
    Page object for the 'Current Licence Needs' widget on the dashboard.
    Covers the Mandatory, Additional, and Selective licence sections.
    """

    PATH = "/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("h3.text-lg.font-semibold.text-gray-900", has_text="Current Licence Needs")
        self.description = page.locator("div.text-sm.text-gray-500").filter(
            has_text="Properties requiring a licence, based on rules in effect today"
        )
        self.badge_mandatory = page.locator("span.fi-badge", has_text="Mandatory")
        self.badge_additional = page.locator("span.fi-badge", has_text="Additional")
        self.badge_selective = page.locator("span.fi-badge", has_text="Selective")

        # Mandatory section links
        self.mandatory_licensed_link = page.locator("a[href*='mandatory'][href*='compliance_status']")
        self.mandatory_applied_link = page.locator("a[href*='mandatory'][href*='licence_requested']")
        self.mandatory_unlicensed_link = page.locator("a[href*='mandatory'][href*='missing_licence']")

        # Additional section links
        self.additional_licensed_link = page.locator("a[href*='additional'][href*='compliance_status']")
        self.additional_applied_link = page.locator("a[href*='additional'][href*='licence_requested']")
        self.additional_unlicensed_link = page.locator("a[href*='additional'][href*='missing_licence']")

        # Selective section links
        self.selective_licensed_link = page.locator("a[href*='selective'][href*='compliance_status']")
        self.selective_applied_link = page.locator("a[href*='selective'][href*='licence_requested']")
        self.selective_unlicensed_link = page.locator("a[href*='selective'][href*='missing_licence']")

    def navigate(self):
        super().navigate(self.PATH)
        self.wait_for_network_idle()
