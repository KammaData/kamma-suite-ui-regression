from playwright.sync_api import Page, expect
from kamma_suite_regression.pages.base_page import BasePage


class DashboardPage(BasePage):
    # TODO: update PATH once the post-login dashboard route is confirmed
    PATH = "/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)
        self.nav = page.locator("nav.fi-sidebar-nav")
        self.heading = page.locator("h1.fi-header-heading")

        # Portfolio Overview section
        self.stat_total_properties = (
            page.locator("div.flex.items-center.justify-between")
            .filter(has=page.get_by_text("Total Properties", exact=True))
            .locator("p.text-3xl")
        )
        self.stat_compliant = (
            page.locator("div.flex.items-center.justify-between")
            .filter(has=page.get_by_text("Compliant", exact=True))
            .locator("span.font-semibold")
        )

        # Priority action cards (links)
        self.properties_in_breach_link = page.locator("a").filter(has=page.locator("h3", has_text="Properties in Breach"))
        self.unrecognised_address_link = page.locator("a").filter(has=page.locator("h3", has_text="Unrecognised Address"))
        self.incomplete_property_info_link = page.locator("a").filter(has=page.locator("h3", has_text="Incomplete Property Information"))
        self.priority_action_cards = page.locator("div.grid > a")

        # Priority action card counts
        self.stat_in_breach_count = self.properties_in_breach_link.locator("p.text-4xl")
        self.stat_verify_address = self.unrecognised_address_link.locator("p.text-4xl")
        self.stat_occupancy = self.incomplete_property_info_link.locator("p.text-4xl")

    def navigate(self):
        super().navigate(self.PATH)
        self.wait_for_network_idle()

    def assert_page_loaded(self):
        """Verify core dashboard elements are present and visible."""
        expect(self.nav).to_be_visible()

    def get_stats(self) -> dict:
        """Return the visible portfolio stat values from the dashboard UI."""
        return {
            "total_properties": self.stat_total_properties.inner_text().strip(),
            "compliant": self.stat_compliant.inner_text().strip(),
            "in_breach_count": self.stat_in_breach_count.inner_text().strip(),
            "verify_address": self.stat_verify_address.inner_text().strip(),
            "occupancy": self.stat_occupancy.inner_text().strip(),
        }
