from playwright.sync_api import Page


class AddPropertyModal:
    def __init__(self, page: Page):
        self.page = page

        _dialog = page.locator("div.fi-modal[role='dialog']")
        self.modal = _dialog

        # All three select fields teleport their dropdown panel to body.
        # Alpine x-show sets inline display:none when closed; the open panel has no such style.
        _open_panel = page.locator("div.fi-dropdown-panel:not([style*='display: none'])")

        # Branch field (button 0)
        self.branch_dropdown = _dialog.locator(".fi-select-input-btn").first
        self.branch_dropdown_search = _open_panel.locator("div.fi-select-input-search-ctn input.fi-input")
        self.branch_dropdown_list = _open_panel.locator("ul.fi-dropdown-list")
        self.branch_dropdown_options = _open_panel.locator("li.fi-dropdown-list-item")

        # Address field (button 1) — type-to-search autocomplete
        self.address_trigger = _dialog.locator(".fi-select-input-btn").nth(1)
        self.address_input = _open_panel.locator("input.fi-input[placeholder*='Type an address']")
        # Exclude the static "Address not in list" sentinel (data-value="custom")
        self.address_suggestions = _open_panel.filter(
            has=page.locator("input[placeholder*='Type an address']")
        ).locator("li[data-value]:not([data-value='custom'])")

        # Property manager field (button 2)
        self.property_manager_dropdown = _dialog.locator(".fi-select-input-btn").nth(2)
        self.property_manager_search = _open_panel.locator("div.fi-select-input-search-ctn input.fi-input")
        self.property_manager_list = _open_panel.locator("ul.fi-dropdown-list")
        self.property_manager_selected_value = _dialog.locator(".fi-select-input-value-ctn").nth(2)

        # Property reference field (dot in ID escaped for CSS)
        self.property_reference_input = page.locator(
            "input#mountedActionSchema0\\.property_ref"
        )

        # Submit / cancel
        self.submit_button = _dialog.locator("button[type='submit']")
        self.cancel_button = _dialog.locator("button", has_text="Cancel")
