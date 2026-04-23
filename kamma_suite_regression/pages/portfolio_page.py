from playwright.sync_api import Page
from kamma_suite_regression.pages.base_page import BasePage


class PortfolioPage(BasePage):
    PATH = "/portfolio"

    def __init__(self, page: Page):
        super().__init__(page)

        # Portfolio overview stats
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
        self.stat_not_compliant = (
            page.locator("div.flex.items-center.justify-between")
            .filter(has=page.get_by_text("Not Compliant", exact=True))
            .locator("span.font-semibold")
        )
        self.compliance_progress_bar = page.locator("div.h-4.w-full.overflow-hidden.rounded-full.bg-gray-200")

        # Branch filter (first custom dropdown)
        self.dropdown_button = page.locator("button.fi-select-input-btn").first
        self.dropdown_list = page.locator("ul.fi-dropdown-list").first
        self.dropdown_search = page.locator("input[aria-label='Search']").first
        self.dropdown_placeholder = page.locator("span.fi-select-input-placeholder").first

        # Authority filter (second custom dropdown)
        self.authority_filter_button = page.locator("button.fi-select-input-btn").nth(1)
        self.authority_filter_list = page.locator("ul.fi-dropdown-list").nth(1)
        self.authority_filter_search = page.locator("input[aria-label='Search']").nth(1)
        self.authority_filter_placeholder = page.locator("span.fi-select-input-placeholder").nth(1)
        self.authority_filter_options = page.locator("ul.fi-dropdown-list").nth(1).locator("li.fi-dropdown-list-item")

        # Property manager filter (multi-select, uses div.fi-select-input-ctn as trigger)
        _pm = page.locator("div.fi-select-input-ctn")
        self.property_manager_container = _pm
        self.property_manager_placeholder = _pm.locator("span.fi-select-input-placeholder")
        self.property_manager_search = _pm.locator("input[aria-label='Search']")
        self.property_manager_list = _pm.locator("ul.fi-dropdown-list")
        self.property_manager_options = _pm.locator("ul.fi-dropdown-list li.fi-dropdown-list-item")

        # Action required filter (third button-based custom dropdown, multi-select)
        self.action_required_label = page.locator("label.fi-fo-field-label", has_text="Action Required")
        self.action_required_button = page.locator("button.fi-select-input-btn").nth(2)
        self.action_required_list = page.locator("ul.fi-dropdown-list").nth(2)
        self.action_required_options = page.locator("ul.fi-dropdown-list").nth(2).locator("li.fi-dropdown-list-item")
        self.action_required_placeholder = page.locator("span.fi-select-input-placeholder").nth(2)
        self.action_required_selected_values = page.locator("span.fi-select-input-value-ctn")

        # Scheme type filter (fourth button-based custom dropdown, multi-select)
        self.scheme_type_filter_button = page.locator("button.fi-select-input-btn").nth(3)
        self.scheme_type_filter_list = page.locator("ul.fi-dropdown-list").nth(3)
        self.scheme_type_filter_options = page.locator("ul.fi-dropdown-list").nth(3).locator("li.fi-dropdown-list-item")
        self.scheme_type_filter_placeholder = page.locator("span.fi-select-input-placeholder").nth(3)
        self.scheme_type_filter_selected_values = page.locator("div.fi-select-input-value-ctn")

        # Licence scheme filter (fifth button-based custom dropdown)
        self.licence_scheme_filter_button = page.locator("button.fi-select-input-btn").nth(4)
        self.licence_scheme_filter_list = page.locator("ul.fi-dropdown-list").nth(4)
        self.licence_scheme_filter_options = page.locator("ul.fi-dropdown-list").nth(4).locator("li.fi-dropdown-list-item")
        self.licence_scheme_filter_placeholder = page.locator("span.fi-select-input-placeholder").nth(4)

        # Compliance status filter
        self.compliance_status_label = page.locator("label[for='tableFiltersForm.compliance_status.value']")
        self.compliance_status_select = page.locator("select#tableFiltersForm\\.compliance_status\\.value")

        # Licence type filter
        self.licence_type_label = page.locator("label.fi-fo-field-label").first
        self.licence_type_select = page.locator("select.fi-select-input").first
        self.licence_type_options = page.locator("select.fi-select-input").first.locator("option")

        # Licence expiry filter (second native select)
        self.licence_expiry_select = page.locator("select.fi-select-input").nth(1)
        self.licence_expiry_options = page.locator("select.fi-select-input").nth(1).locator("option")

        # Upcoming schemes filter
        self.upcoming_schemes_label = page.locator("label.fi-fo-field-label", has_text="Upcoming Schemes")
        self.upcoming_schemes_select = page.locator(
            "xpath=//label[contains(@class,'fi-fo-field-label')][normalize-space()='Upcoming Schemes']"
            "/parent::*/descendant::select[contains(@class,'fi-select-input')]"
        )
        self.upcoming_schemes_options = page.locator(
            "xpath=//label[contains(@class,'fi-fo-field-label')][normalize-space()='Upcoming Schemes']"
            "/parent::*/descendant::select[contains(@class,'fi-select-input')]/option"
        )

        # Properties table
        self.table = page.locator("table.fi-ta-table")
        self.table_rows = page.locator("tr.fi-ta-row")

        # Column headers (fi-ta-header-cell is always present as base class)
        self.col_header_id = page.locator("th.fi-ta-header-cell", has_text="ID")
        self.col_header_address = page.locator("th.fi-ta-header-cell", has_text="Address")
        self.col_header_authority = page.locator("th.fi-ta-header-cell", has_text="Local Authority")
        self.col_header_schemes = page.locator("th.fi-ta-header-cell", has_text="Current Schemes")
        self.col_header_licence_required = page.locator("th.fi-ta-header-cell-compliancy\\.licence-required")
        self.col_header_upcoming_licence = page.locator("th.fi-ta-header-cell", has_text="Upcoming Licence Required")
        self.col_header_people = page.locator("th.fi-ta-header-cell", has_text="People")
        self.col_header_households = page.locator("th.fi-ta-header-cell", has_text="Households")
        self.col_header_compliance_status = page.locator("th.fi-ta-header-cell", has_text="Compliance Status")
        self.col_header_actions = page.locator("th.fi-ta-actions-header-cell")

        # Column cells (dot in class name escaped for CSS selector)
        self.cells_schemes = page.locator("td.fi-ta-cell-schemes")
        self.cells_licence_required = page.locator("td.fi-ta-cell-compliancy\\.licence-required")
        self.cells_upcoming_licence = page.locator("td.fi-ta-cell-compliancy\\.licence-required-future")
        self.cells_compliance_status = page.locator("td.fi-ta-cell-compliancy\\.compliant")

        # Add property action
        self.add_property_button = page.locator("button[wire\\:click=\"mountAction('add_property')\"]")

        # Priority action cards
        self.properties_in_breach_link = page.locator("a").filter(has=page.locator("h3", has_text="Properties in Breach"))
        self.unrecognised_address_link = page.locator("a").filter(has=page.locator("h3", has_text="Unrecognised Address"))
        self.incomplete_property_info_link = page.locator("a").filter(has=page.locator("h3", has_text="Incomplete Property Information"))
        self.affected_by_upcoming_scheme_link = page.locator("a").filter(has=page.locator("h3", has_text="Affected by Upcoming Scheme"))
        self.priority_action_cards = page.locator("div.grid > a")

    def navigate(self, filters: str = None):
        path = f"{self.PATH}?{filters}" if filters else self.PATH
        super().navigate(path)
        self.wait_for_network_idle()
