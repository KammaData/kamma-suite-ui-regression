"""
Add Property modal tests.

Route: /portfolio
Coverage:
  - Modal opens on button click
  - Branch dropdown is present and functional
  - Address input is present and accepts text
  - Property manager dropdown is present and functional
  - Property reference input is present
  - Submit button is present
  - Submitting an empty form triggers validation
"""

import re
import uuid
import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.portfolio_page import PortfolioPage
from kamma_suite_regression.pages.add_property_modal import AddPropertyModal


@pytest.fixture
def open_modal(authenticated_page):
    """Navigate to portfolio and open the Add New Property modal."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.add_property_button.click()
    authenticated_page.wait_for_load_state("networkidle")
    modal = AddPropertyModal(authenticated_page)
    expect(modal.modal).to_have_class(re.compile("fi-modal-open"))
    return modal


@pytest.mark.smoke
@pytest.mark.dashboard
def test_add_property_modal_opens(authenticated_page):
    """Verify the Add New Property modal opens on button click."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.add_property_button.click()
    authenticated_page.wait_for_load_state("networkidle")
    expect(authenticated_page.locator("div.fi-modal[role='dialog']")).to_have_class(re.compile("fi-modal-open"))


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_submit_button_visible(open_modal):
    """Verify the submit button is visible inside the modal."""
    expect(open_modal.submit_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_branch_dropdown_visible(open_modal):
    """Verify the branch dropdown is visible inside the modal."""
    expect(open_modal.branch_dropdown).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_branch_dropdown_opens(open_modal):
    """Verify typing in the branch dropdown search reveals the options list."""
    open_modal.branch_dropdown.click()
    open_modal.branch_dropdown_search.fill("a")
    expect(open_modal.branch_dropdown_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_branch_dropdown_has_options(open_modal):
    """Verify the branch dropdown contains at least one option after searching."""
    open_modal.branch_dropdown.click()
    open_modal.branch_dropdown_search.fill("a")
    expect(open_modal.branch_dropdown_list).to_be_visible()
    assert open_modal.branch_dropdown_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_address_trigger_visible(open_modal):
    """Verify the address field trigger is visible inside the modal."""
    expect(open_modal.address_trigger).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_address_input_visible(open_modal):
    """Verify the address input is visible after opening the address field."""
    open_modal.address_trigger.click()
    expect(open_modal.address_input).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_address_input_accepts_text(open_modal):
    """Verify the address input accepts typed text."""
    open_modal.address_trigger.click()
    open_modal.address_input.fill("10 Church Lane")
    expect(open_modal.address_input).to_have_value("10 Church Lane")


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_address_search_shows_suggestions(open_modal):
    """Verify typing in the address input triggers autocomplete suggestions."""
    open_modal.address_trigger.click()
    open_modal.address_input.fill("10 Church")
    expect(open_modal.address_suggestions.first).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_property_manager_dropdown_visible(open_modal):
    """Verify the property manager dropdown is visible inside the modal."""
    expect(open_modal.property_manager_dropdown).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_property_manager_dropdown_opens(open_modal):
    """Verify clicking the property manager dropdown reveals the options list."""
    open_modal.property_manager_dropdown.click()
    expect(open_modal.property_manager_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_property_manager_accepts_selection(open_modal):
    """Verify selecting an option from the property manager dropdown updates the displayed value."""
    open_modal.property_manager_dropdown.click()
    expect(open_modal.property_manager_list).to_be_visible()
    open_modal.property_manager_list.locator("li").first.click()
    expect(open_modal.property_manager_selected_value).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_property_reference_input_visible(open_modal):
    """Verify the property reference input is visible inside the modal."""
    expect(open_modal.property_reference_input).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_submit_triggers_validation(open_modal):
    """Verify submitting the empty form keeps the modal open (form-level validation)."""
    open_modal.submit_button.click()
    open_modal.page.wait_for_load_state("networkidle")
    expect(open_modal.modal).to_have_class(re.compile("fi-modal-open"))


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_cancel_button_visible(open_modal):
    """Verify the Cancel button is visible inside the modal."""
    expect(open_modal.cancel_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_cancel_button_closes_modal(open_modal):
    """Verify clicking Cancel closes the modal."""
    open_modal.cancel_button.click()
    expect(open_modal.modal).not_to_have_class(re.compile("fi-modal-open"))


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_submit_button_is_enabled(open_modal):
    """Verify the submit button is enabled when the modal first opens."""
    expect(open_modal.submit_button).to_be_enabled()


@pytest.mark.regression
@pytest.mark.dashboard
def test_add_property_valid_submission_navigates_to_property(authenticated_page, base_url):
    """Verify submitting the form with a valid address navigates to the new property page."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.add_property_button.click()
    authenticated_page.wait_for_load_state("networkidle")

    modal = AddPropertyModal(authenticated_page)
    expect(modal.modal).to_have_class(re.compile("fi-modal-open"))

    modal.address_trigger.click()
    modal.address_input.fill("24 charles street, oxford, ox4 3as")
    expect(modal.address_suggestions.first).to_be_visible()
    modal.address_suggestions.first.click()
    authenticated_page.wait_for_load_state("networkidle")

    modal.property_reference_input.fill(uuid.uuid4().hex[:8])
    modal.submit_button.click()

    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio/kamma:property:"),
        timeout=30_000,
    )
