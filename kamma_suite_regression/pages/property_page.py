from playwright.sync_api import Page
from kamma_suite_regression.pages.base_page import BasePage


class PropertyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Page header
        self.page_heading = page.locator("h1", has_text="Property Compliance Overview")
        self.address_heading = page.locator("h1").nth(1)

        # Header action buttons
        self.edit_button = page.locator("button[wire\\:click=\"mountAction('edit_property')\"]")
        self.delete_button = page.locator("button[wire\\:click=\"mountAction('delete')\"]")

        # Filament action modal — dynamic id like fi-{hash}-action-0
        self.edit_property_modal = page.locator("div.fi-modal[id$='-action-0']")

        # Compliance Status section
        _compliance = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Compliance Status")
        )
        self.compliance_status_section = _compliance
        self.compliance_status_badge = _compliance.locator(".fi-badge")

        # Action card (heading starts with "Action:")
        self.action_card = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Action:")
        )

        # Licence Requirement section
        _lic_req = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Licence Requirement")
        )
        self.licence_requirement_section = _lic_req
        self.licence_requirement_badge = _lic_req.locator(".fi-badge")

        # Active licensing schemes section
        _active = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Active licensing schemes")
        )
        self.active_schemes_section = _active
        self.active_scheme_badges = _active.locator(".fi-badge")

        # Tenancy Details section
        _tenancy = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Tenancy Details")
        )
        self.tenancy_section = _tenancy
        self.tenancy_occupants_input = _tenancy.locator("input[type='number']").first
        self.tenancy_households_input = _tenancy.locator("input[type='number']").nth(1)
        self.tenancy_update_button = _tenancy.locator("button", has_text="Update")

        # Attributes section
        _attrs = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Attributes")
        )
        self.attributes_section = _attrs
        self.attributes_storeys_input = _attrs.locator("input[type='number']")
        self.attributes_category_select = _attrs.locator("select")
        self.attributes_update_button = _attrs.locator("button", has_text="Update")

        # Licence Management section
        _lic_mgmt = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Licence Management")
        )
        self.licence_management_section = _lic_mgmt
        self.log_application_button = page.locator("button[wire\\:click='openApplyModal']")
        self.upload_licence_button = page.locator("button[wire\\:click='openUploadModal']")
        self.add_exemption_button = page.locator("button[wire\\:click='openExemptionModal']")

        # Modal submit buttons (present in DOM but inside hidden modals)
        self.log_application_submit = page.locator("button[wire\\:click='submitApplication']")
        self.upload_licence_submit = page.locator("button[wire\\:click='submitLicence']")
        self.add_exemption_submit = page.locator("button[wire\\:click='submitExemption']")

        # Log Application modal fields
        _apply = page.locator("#apply-licence-modal")
        self.apply_modal = _apply
        self.apply_licence_type_select = _apply.locator("select#applicationForm\\.licence_type")
        self.apply_application_date = _apply.locator("input#applicationForm\\.application_date")
        self.apply_application_ref = _apply.locator("input#applicationForm\\.application_ref")
        self.apply_close_button = _apply.locator("button.fi-modal-close-btn")

        # Upload Licence modal fields
        _upload = page.locator("#licence-modal")
        self.upload_modal = _upload
        self.upload_licence_type_select = _upload.locator("select#licenceForm\\.licence_type")
        self.upload_status_granted = _upload.locator("input#licenceForm\\.licence_status-granted")
        self.upload_status_rejected = _upload.locator("input#licenceForm\\.licence_status-rejected")
        self.upload_start_date = _upload.locator("input#licenceForm\\.licence_start_date")
        self.upload_expiry_date = _upload.locator("input#licenceForm\\.licence_expiry_date")
        self.upload_max_occupants = _upload.locator("input#licenceForm\\.max_occupants")
        self.upload_max_households = _upload.locator("input#licenceForm\\.max_households")
        self.upload_named_licensee = _upload.locator("input#licenceForm\\.named_licensee")
        self.upload_document_ref = _upload.locator("input#licenceForm\\.document_ref")
        self.upload_file_input = _upload.locator("input[type='file']")
        self.upload_close_button = _upload.locator("button.fi-modal-close-btn")

        # Add Exemption modal fields
        _exempt = page.locator("#exemption-modal")
        self.exemption_modal = _exempt
        self.exemption_reason = _exempt.locator("input#exemptionForm\\.reason")
        self.exemption_determination_type = _exempt.locator("select#exemptionForm\\.determination_type")
        self.exemption_date_end = _exempt.locator("input#exemptionForm\\.determination_date_end")
        self.exemption_close_button = _exempt.locator("button.fi-modal-close-btn")

        # Licensing Schemes section
        _schemes = page.locator(".fi-section").filter(
            has=page.get_by_role("heading", level=3, name="Licensing Schemes", exact=True)
        )
        self.licensing_schemes_section = _schemes
        self.current_schemes_heading = _schemes.locator("h4", has_text="Current Schemes")
        self.licensing_schemes_table = _schemes.locator("table")
        self.licensing_schemes_rows = _schemes.locator("tbody tr")

        # Notes section (collapsible)
        _notes = page.locator(".fi-section").filter(
            has=page.locator("h3", has_text="Notes")
        )
        self.notes_section = _notes
        self.notes_toggle = _notes.locator("button").first
        self.notes_textarea = _notes.locator("textarea")
        self.notes_revert_button = _notes.locator("button", has_text="Revert")
        self.notes_update_button = _notes.locator("button", has_text="Update")

    def navigate(self, property_id: str):
        super().navigate(f"/portfolio/{property_id}")
        self.wait_for_network_idle()
