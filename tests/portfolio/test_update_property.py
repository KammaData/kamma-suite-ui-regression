"""
Property detail page tests.

Route: /portfolio/{kamma_id}
Coverage:
  - Page loads with correct title and address
  - Edit and Delete action buttons
  - Compliance Status section
  - Action card
  - Licence Requirement section
  - Active Licensing Schemes section
  - Tenancy Details section (view and update)
  - Attributes section (view and update)
  - Licence Management section and modals
  - Licensing Schemes table
  - Notes section (toggle and update)
  - Property reference displayed in summary
"""

import re
import uuid
import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.property_page import PropertyPage
from kamma_suite_regression.api.helpers.properties_helper import PropertiesHelper


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def created_property(api_v3):
    """Create a property once for the module, delete it on teardown."""
    helper = PropertiesHelper(api_v3)
    ref = f"ui-test-{uuid.uuid4().hex[:8]}"
    result = helper.create_property({
        "properties": [{
            "external_id": ref,
            "address": {
                "postcode": "OX4 3AS",
                "address": "24 CHARLES STREET, OXFORD, OX4 3AS",
            },
            "classification": {},
            "details": {},
        }]
    })
    kamma_id = result["results"][0]["id"]
    yield {"id": kamma_id, "ref": ref}
    try:
        helper.delete_property(kamma_id)
    except Exception:
        pass


@pytest.fixture
def property_page(authenticated_page, created_property):
    """Navigate to the created property page before each test."""
    prop = PropertyPage(authenticated_page)
    prop.navigate(created_property["id"])
    return prop


# ---------------------------------------------------------------------------
# Page load
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_property_page_title(property_page):
    """Page heading reads 'Property Compliance Overview'."""
    expect(property_page.page_heading).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_property_page_address_heading(property_page):
    """Address is shown as a top-level heading."""
    expect(property_page.address_heading).to_be_visible()
    expect(property_page.address_heading).to_have_text(re.compile(r"CHARLES STREET", re.IGNORECASE))


@pytest.mark.regression
@pytest.mark.properties
def test_property_url_contains_kamma_id(authenticated_page, created_property, base_url):
    """Navigating to the property routes to the correct URL."""
    prop = PropertyPage(authenticated_page)
    prop.navigate(created_property["id"])
    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio/{re.escape(created_property['id'])}")
    )


@pytest.mark.regression
@pytest.mark.properties
def test_property_ref_visible_in_summary(property_page, created_property):
    """The external_id (property reference) is displayed on the page."""
    expect(property_page.page.get_by_text(created_property["ref"]).first).to_be_visible()


# ---------------------------------------------------------------------------
# Header actions
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_edit_property_button_visible(property_page):
    """Edit Property button is visible in the page header."""
    expect(property_page.edit_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_delete_property_button_visible(property_page):
    """Delete Property button is visible in the page header."""
    expect(property_page.delete_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_edit_property_opens_modal(property_page):
    """Clicking Edit Property opens the edit modal."""
    property_page.edit_button.click()
    property_page.page.wait_for_load_state("networkidle")
    expect(property_page.edit_property_modal).to_have_class(re.compile("fi-modal-open"))


@pytest.mark.regression
@pytest.mark.properties
def test_delete_property_opens_confirmation(property_page):
    """Clicking Delete Property opens a confirmation modal."""
    property_page.delete_button.click()
    property_page.page.wait_for_load_state("networkidle")
    expect(property_page.edit_property_modal).to_have_class(re.compile("fi-modal-open"))


# ---------------------------------------------------------------------------
# Compliance Status
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_compliance_status_section_visible(property_page):
    """Compliance Status section is rendered on the page."""
    expect(property_page.compliance_status_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_compliance_status_badge_visible(property_page):
    """A compliance status badge is visible inside the section."""
    expect(property_page.compliance_status_badge).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_compliance_status_badge_has_valid_value(property_page):
    """Compliance status badge contains a known value."""
    valid = {"Compliant", "Non-compliant"}
    badge_text = property_page.compliance_status_badge.inner_text().strip()
    assert badge_text in valid, f"Unexpected compliance status: '{badge_text}'"


# ---------------------------------------------------------------------------
# Action card
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_action_card_visible(property_page):
    """An action card is visible on the page."""
    expect(property_page.action_card).to_be_visible()


# ---------------------------------------------------------------------------
# Licence Requirement
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_licence_requirement_section_visible(property_page):
    """Licence Requirement section is rendered."""
    expect(property_page.licence_requirement_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_licence_requirement_badge_visible(property_page):
    """Licence requirement badge is visible inside the section."""
    expect(property_page.licence_requirement_badge).to_be_visible()


# ---------------------------------------------------------------------------
# Active Licensing Schemes
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_active_schemes_section_visible(property_page):
    """Active licensing schemes section is rendered."""
    expect(property_page.active_schemes_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_active_schemes_has_at_least_one_badge(property_page):
    """At least one licensing scheme badge is shown."""
    assert property_page.active_scheme_badges.count() > 0


# ---------------------------------------------------------------------------
# Tenancy Details
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_tenancy_details_section_visible(property_page):
    """Tenancy Details section is rendered."""
    expect(property_page.tenancy_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_tenancy_occupants_input_visible(property_page):
    """Occupants number input is visible in Tenancy Details."""
    expect(property_page.tenancy_occupants_input).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_tenancy_households_input_visible(property_page):
    """Households number input is visible in Tenancy Details."""
    expect(property_page.tenancy_households_input).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_tenancy_update_button_visible(property_page):
    """Update button is visible in Tenancy Details."""
    expect(property_page.tenancy_update_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_tenancy_update_button_enabled(property_page):
    """Update button is enabled in Tenancy Details."""
    expect(property_page.tenancy_update_button).to_be_enabled()


@pytest.mark.regression
@pytest.mark.properties
def test_tenancy_details_can_update_occupants(property_page):
    """Filling occupants and clicking Update keeps the page open (no nav away)."""
    property_page.tenancy_occupants_input.fill("3")
    property_page.tenancy_households_input.fill("1")
    property_page.tenancy_update_button.click()
    property_page.page.wait_for_load_state("networkidle")
    expect(property_page.tenancy_section).to_be_visible()


# ---------------------------------------------------------------------------
# Attributes
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_attributes_section_visible(property_page):
    """Attributes section is rendered."""
    expect(property_page.attributes_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_attributes_storeys_input_visible(property_page):
    """Storeys number input is visible in Attributes."""
    expect(property_page.attributes_storeys_input).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_attributes_category_select_visible(property_page):
    """Property Category select is visible in Attributes."""
    expect(property_page.attributes_category_select).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_attributes_update_button_visible(property_page):
    """Update button is visible in Attributes."""
    expect(property_page.attributes_update_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_attributes_update_button_enabled(property_page):
    """Update button is enabled in Attributes."""
    expect(property_page.attributes_update_button).to_be_enabled()


# ---------------------------------------------------------------------------
# Licence Management
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_licence_management_section_visible(property_page):
    """Licence Management section is rendered."""
    expect(property_page.licence_management_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_log_application_button_visible(property_page):
    """'Log an Application' button is visible."""
    expect(property_page.log_application_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_upload_licence_button_visible(property_page):
    """'Upload a Licence' button is visible."""
    expect(property_page.upload_licence_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_add_exemption_button_visible(property_page):
    """'Add Licence Exemption' button is visible."""
    expect(property_page.add_exemption_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_log_application_opens_modal(property_page):
    """Clicking 'Log an Application' reveals the modal submit button."""
    property_page.log_application_button.click()
    expect(property_page.log_application_submit).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_upload_licence_opens_modal(property_page):
    """Clicking 'Upload a Licence' reveals the modal submit button."""
    property_page.upload_licence_button.click()
    expect(property_page.upload_licence_submit).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_add_exemption_opens_modal(property_page):
    """Clicking 'Add Licence Exemption' reveals the modal submit button."""
    property_page.add_exemption_button.click()
    expect(property_page.add_exemption_submit).to_be_visible()


# ---------------------------------------------------------------------------
# Log Application modal fields
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_log_application_modal_fields(property_page):
    """Log Application modal renders all fields and closes correctly."""
    property_page.log_application_button.click()
    expect(property_page.apply_licence_type_select).to_be_visible()
    expect(property_page.apply_application_date).to_be_visible()
    expect(property_page.apply_application_ref).to_be_visible()
    expect(property_page.log_application_submit).to_be_visible()
    property_page.apply_close_button.click()
    expect(property_page.log_application_submit).not_to_be_visible()


# ---------------------------------------------------------------------------
# Upload Licence modal fields
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_upload_licence_modal_fields(property_page):
    """Upload Licence modal renders all fields and closes correctly."""
    property_page.upload_licence_button.click()
    expect(property_page.upload_licence_type_select).to_be_visible()
    expect(property_page.upload_status_granted).to_be_visible()
    expect(property_page.upload_status_rejected).to_be_visible()
    expect(property_page.upload_start_date).to_be_visible()
    expect(property_page.upload_expiry_date).to_be_visible()
    expect(property_page.upload_max_occupants).to_be_visible()
    expect(property_page.upload_max_households).to_be_visible()
    expect(property_page.upload_named_licensee).to_be_visible()
    expect(property_page.upload_document_ref).to_be_visible()
    expect(property_page.upload_file_input).to_be_attached()
    expect(property_page.upload_licence_submit).to_be_visible()
    property_page.upload_close_button.click()
    expect(property_page.upload_licence_submit).not_to_be_visible()


# ---------------------------------------------------------------------------
# Add Exemption modal fields
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_add_exemption_modal_fields(property_page):
    """Add Exemption modal renders all fields and closes correctly."""
    property_page.add_exemption_button.click()
    expect(property_page.exemption_reason).to_be_visible()
    expect(property_page.exemption_determination_type).to_be_visible()
    expect(property_page.exemption_date_end).to_be_visible()
    expect(property_page.add_exemption_submit).to_be_visible()
    property_page.exemption_close_button.click()
    expect(property_page.add_exemption_submit).not_to_be_visible()


# ---------------------------------------------------------------------------
# Licensing Schemes table
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.properties
def test_licensing_schemes_section_visible(property_page):
    """Licensing Schemes section is rendered."""
    expect(property_page.licensing_schemes_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_current_schemes_heading_visible(property_page):
    """'Current Schemes' sub-heading is visible inside the section."""
    expect(property_page.current_schemes_heading).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_licensing_schemes_table_visible(property_page):
    """The licensing schemes table is rendered."""
    expect(property_page.licensing_schemes_table).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_licensing_schemes_table_has_rows(property_page):
    """The licensing schemes table has at least one data row."""
    assert property_page.licensing_schemes_rows.count() > 0


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.properties
def test_notes_section_visible(property_page):
    """Notes section is rendered."""
    expect(property_page.notes_section).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_notes_toggle_visible(property_page):
    """Notes toggle button is visible."""
    expect(property_page.notes_toggle).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_notes_expands_on_click(property_page):
    """Clicking the Notes toggle reveals the textarea and Update button."""
    property_page.notes_toggle.click()
    property_page.page.wait_for_timeout(1000)
    expect(property_page.notes_textarea).to_be_visible()
    expect(property_page.notes_update_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_notes_textarea_visible_when_expanded(property_page):
    """The notes textarea is accessible after expanding the section."""
    property_page.notes_toggle.click()
    property_page.page.wait_for_timeout(1000)
    expect(property_page.notes_textarea).to_be_visible()


@pytest.mark.regression
@pytest.mark.properties
def test_notes_update_button_disabled_when_unchanged(property_page):
    """Notes Update button is disabled when notes have not been edited."""
    property_page.notes_toggle.click()
    property_page.page.wait_for_timeout(1000)
    expect(property_page.notes_update_button).to_be_disabled()


@pytest.mark.regression
@pytest.mark.properties
def test_notes_update_button_enabled_after_edit(property_page):
    """Notes Update button becomes enabled after editing the textarea."""
    property_page.notes_toggle.click()
    property_page.page.wait_for_timeout(1000)
    property_page.notes_textarea.fill("Automated test note")
    expect(property_page.notes_update_button).to_be_enabled()
