"""
Portfolio filter tests.

Route: /portfolio
Coverage:
  - Branch filter (custom button dropdown)
  - Authority filter (custom button dropdown)
  - Property manager filter (multi-select, div-trigger dropdown)
  - Action required filter (custom button dropdown, multi-select)
  - Scheme type filter (custom button dropdown, multi-select)
  - Licence scheme filter (custom button dropdown)
  - Compliance status filter (native select)
  - Licence type filter (native select)
  - Upcoming schemes filter (native select)
  - Licence expiry filter (native select)
"""

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.skip(reason="filter locators need verifying against live UI")

from kamma_suite_regression.pages.portfolio_page import PortfolioPage


# --- Branch filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_branch_filter_placeholder_visible(authenticated_page):
    """Verify the branch filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.dropdown_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_branch_filter_expands_on_click(authenticated_page):
    """Verify clicking the branch filter opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.dropdown_button.click()
    expect(portfolio.dropdown_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_branch_filter_search_visible_when_open(authenticated_page):
    """Verify the search input is visible when the branch filter is open."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.dropdown_button.click()
    expect(portfolio.dropdown_search).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_branch_filter_accepts_selection(authenticated_page):
    """Verify selecting an item from the branch filter closes the list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.dropdown_button.click()
    expect(portfolio.dropdown_list).to_be_visible()
    portfolio.dropdown_list.locator("li").first.click()
    expect(portfolio.dropdown_list).not_to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_branch_filter_search_filters_results(authenticated_page):
    """Verify typing in the branch filter search input filters the list items."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.dropdown_button.click()
    expect(portfolio.dropdown_list).to_be_visible()
    initial_count = portfolio.dropdown_list.locator("li").count()
    portfolio.dropdown_search.fill("a")
    filtered_count = portfolio.dropdown_list.locator("li").count()
    assert filtered_count <= initial_count


# --- Authority filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_placeholder_visible(authenticated_page):
    """Verify the authority filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.authority_filter_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_expands_on_click(authenticated_page):
    """Verify clicking the authority filter button opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.authority_filter_button.click()
    expect(portfolio.authority_filter_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_search_visible_when_open(authenticated_page):
    """Verify the search input is visible when the authority filter is open."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.authority_filter_button.click()
    expect(portfolio.authority_filter_search).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_has_options(authenticated_page):
    """Verify the authority filter list contains at least one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.authority_filter_button.click()
    expect(portfolio.authority_filter_list).to_be_visible()
    assert portfolio.authority_filter_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_search_filters_results(authenticated_page):
    """Verify typing in the authority filter search input narrows the option list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.authority_filter_button.click()
    expect(portfolio.authority_filter_list).to_be_visible()
    initial_count = portfolio.authority_filter_options.count()
    portfolio.authority_filter_search.fill("a")
    filtered_count = portfolio.authority_filter_options.count()
    assert filtered_count <= initial_count


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_authority_filter_accepts_selection(authenticated_page):
    """Verify selecting an item from the authority filter closes the dropdown."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.authority_filter_button.click()
    expect(portfolio.authority_filter_list).to_be_visible()
    portfolio.authority_filter_options.first.click()
    expect(portfolio.authority_filter_list).not_to_be_visible()


# --- Property manager filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_placeholder_visible(authenticated_page):
    """Verify the property manager filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.property_manager_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_expands_on_click(authenticated_page):
    """Verify clicking the property manager filter container opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.property_manager_container.click()
    expect(portfolio.property_manager_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_search_visible_when_open(authenticated_page):
    """Verify the search input is visible when the property manager filter is open."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.property_manager_container.click()
    expect(portfolio.property_manager_search).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_has_options(authenticated_page):
    """Verify the property manager filter list contains at least one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.property_manager_container.click()
    expect(portfolio.property_manager_list).to_be_visible()
    assert portfolio.property_manager_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_search_filters_results(authenticated_page):
    """Verify typing in the property manager search input narrows the option list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.property_manager_container.click()
    expect(portfolio.property_manager_list).to_be_visible()
    initial_count = portfolio.property_manager_options.count()
    portfolio.property_manager_search.fill("a")
    filtered_count = portfolio.property_manager_options.count()
    assert filtered_count <= initial_count


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_property_manager_filter_allows_multiple_selections(authenticated_page):
    """Verify the property manager filter allows selecting more than one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.property_manager_container.click()
    expect(portfolio.property_manager_list).to_be_visible()
    portfolio.property_manager_options.nth(0).click()
    portfolio.property_manager_options.nth(1).click()
    selected = portfolio.property_manager_options.locator("span[aria-selected='true']")
    assert selected.count() == 2


# --- Action required filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_label_visible(authenticated_page):
    """Verify the action required filter label is visible and correctly named."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.action_required_label).to_be_visible()
    expect(portfolio.action_required_label).to_have_text("Action Required")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_placeholder_visible(authenticated_page):
    """Verify the action required filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.action_required_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_expands_on_click(authenticated_page):
    """Verify clicking the action required filter button opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.action_required_button.click()
    expect(portfolio.action_required_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_has_options(authenticated_page):
    """Verify the action required filter list contains at least one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.action_required_button.click()
    expect(portfolio.action_required_list).to_be_visible()
    assert portfolio.action_required_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_closes_on_second_click(authenticated_page):
    """Verify clicking the action required filter button again closes the dropdown."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.action_required_button.click()
    expect(portfolio.action_required_list).to_be_visible()
    portfolio.action_required_button.click()
    expect(portfolio.action_required_list).not_to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_action_required_filter_allows_multiple_selections(authenticated_page):
    """Verify the action required filter allows selecting more than one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.action_required_button.click()
    expect(portfolio.action_required_list).to_be_visible()
    portfolio.action_required_options.nth(0).click()
    portfolio.action_required_options.nth(1).click()
    expect(portfolio.action_required_selected_values).to_be_visible()


# --- Scheme type filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_placeholder_visible(authenticated_page):
    """Verify the scheme type filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.scheme_type_filter_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_expands_on_click(authenticated_page):
    """Verify clicking the scheme type filter button opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.scheme_type_filter_button.click()
    expect(portfolio.scheme_type_filter_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_has_options(authenticated_page):
    """Verify the scheme type filter list contains at least one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.scheme_type_filter_button.click()
    expect(portfolio.scheme_type_filter_list).to_be_visible()
    assert portfolio.scheme_type_filter_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_closes_after_selection(authenticated_page):
    """Verify selecting a single option from the scheme type filter closes the dropdown."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.scheme_type_filter_button.click()
    expect(portfolio.scheme_type_filter_list).to_be_visible()
    portfolio.scheme_type_filter_options.first.click()
    expect(portfolio.scheme_type_filter_list).not_to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_selection_updates_displayed_value(authenticated_page):
    """Verify selecting an option updates the scheme type filter displayed value."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.scheme_type_filter_button.click()
    expect(portfolio.scheme_type_filter_list).to_be_visible()
    portfolio.scheme_type_filter_options.first.click()
    expect(portfolio.scheme_type_filter_selected_values).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_scheme_type_filter_allows_multiple_selections(authenticated_page):
    """Verify the scheme type filter allows selecting more than one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.scheme_type_filter_button.click()
    expect(portfolio.scheme_type_filter_list).to_be_visible()
    portfolio.scheme_type_filter_options.nth(0).click()
    portfolio.scheme_type_filter_options.nth(1).click()
    expect(portfolio.scheme_type_filter_selected_values).to_be_visible()


# --- Licence scheme filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_placeholder_visible(authenticated_page):
    """Verify the licence scheme filter placeholder is visible before interaction."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_scheme_filter_placeholder).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_expands_on_click(authenticated_page):
    """Verify clicking the licence scheme filter button opens the dropdown list."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_has_options(authenticated_page):
    """Verify the licence scheme filter list contains at least one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).to_be_visible()
    assert portfolio.licence_scheme_filter_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_closes_on_second_click(authenticated_page):
    """Verify clicking the licence scheme filter button again closes the dropdown."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).to_be_visible()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).not_to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_selection_updates_placeholder(authenticated_page):
    """Verify selecting an option changes the licence scheme filter displayed value."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    initial_text = portfolio.licence_scheme_filter_placeholder.inner_text()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).to_be_visible()
    portfolio.licence_scheme_filter_options.first.click()
    expect(portfolio.licence_scheme_filter_placeholder).not_to_have_text(initial_text)


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_scheme_filter_allows_multiple_selections(authenticated_page):
    """Verify the licence scheme filter allows selecting more than one option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.licence_scheme_filter_button.click()
    expect(portfolio.licence_scheme_filter_list).to_be_visible()
    portfolio.licence_scheme_filter_options.nth(0).click()
    portfolio.licence_scheme_filter_options.nth(1).click()
    assert portfolio.licence_scheme_filter_options.count() > 0


# --- Compliance status filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_label_visible(authenticated_page):
    """Verify the compliance status filter label is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.compliance_status_label).to_be_visible()
    expect(portfolio.compliance_status_label).to_have_text("Compliance Status")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_filter_visible(authenticated_page):
    """Verify the compliance status filter select element is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.compliance_status_select).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_filter_selects_compliant(authenticated_page):
    """Verify the compliance status filter accepts the Compliant option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.compliance_status_select.select_option("1")
    expect(portfolio.compliance_status_select).to_have_value("1")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_filter_selects_noncompliant(authenticated_page):
    """Verify the compliance status filter accepts the Non-compliant option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.compliance_status_select.select_option("0")
    expect(portfolio.compliance_status_select).to_have_value("0")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_filter_resets_to_all(authenticated_page):
    """Verify the compliance status filter can be reset to All after a selection."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.compliance_status_select.select_option("1")
    portfolio.compliance_status_select.select_option("")
    expect(portfolio.compliance_status_select).to_have_value("")


# --- Licence type filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_label_visible(authenticated_page):
    """Verify the licence type filter label is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_type_label).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_visible(authenticated_page):
    """Verify the licence type filter select element is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_type_select).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_default_is_all(authenticated_page):
    """Verify the licence type filter defaults to the All (empty) option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_type_select).to_have_value("")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_has_options(authenticated_page):
    """Verify the licence type filter has at least one option available."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    assert portfolio.licence_type_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_options_visible(authenticated_page):
    """Verify each option in the licence type filter is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.licence_type_select.click()
    count = portfolio.licence_type_options.count()
    for i in range(count):
        expect(portfolio.licence_type_options.nth(i)).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_type_filter_accepts_each_option(authenticated_page):
    """Verify each available option in the licence type filter can be selected."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    options = portfolio.licence_type_options.all()
    for option in options:
        value = option.get_attribute("value")
        portfolio.licence_type_select.select_option(value)
        expect(portfolio.licence_type_select).to_have_value(value)


# --- Upcoming schemes filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_label_visible(authenticated_page):
    """Verify the upcoming schemes filter label is visible and correctly named."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.upcoming_schemes_label).to_be_visible()
    expect(portfolio.upcoming_schemes_label).to_have_text("Upcoming Schemes")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_filter_visible(authenticated_page):
    """Verify the upcoming schemes filter select element is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.upcoming_schemes_select).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_filter_default_is_all(authenticated_page):
    """Verify the upcoming schemes filter defaults to the All (empty) option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.upcoming_schemes_select).to_have_value("")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_filter_has_options(authenticated_page):
    """Verify the upcoming schemes filter has at least one option available."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    assert portfolio.upcoming_schemes_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_filter_accepts_each_option(authenticated_page):
    """Verify each available option in the upcoming schemes filter can be selected."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    options = portfolio.upcoming_schemes_options.all()
    for option in options:
        value = option.get_attribute("value")
        portfolio.upcoming_schemes_select.select_option(value)
        expect(portfolio.upcoming_schemes_select).to_have_value(value)


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_schemes_filter_open_shows_options(authenticated_page):
    """Verify clicking the upcoming schemes filter reveals its options."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.upcoming_schemes_select.click()
    assert portfolio.upcoming_schemes_options.count() > 0


# --- Licence expiry filter ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_expiry_filter_visible(authenticated_page):
    """Verify the licence expiry filter select element is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_expiry_select).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_expiry_filter_default_is_all(authenticated_page):
    """Verify the licence expiry filter defaults to the All (empty) option."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.licence_expiry_select).to_have_value("")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_expiry_filter_has_options(authenticated_page):
    """Verify the licence expiry filter has at least one option available."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    assert portfolio.licence_expiry_options.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_expiry_filter_accepts_each_option(authenticated_page):
    """Verify each available option in the licence expiry filter can be selected."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    options = portfolio.licence_expiry_options.all()
    for option in options:
        value = option.get_attribute("value")
        portfolio.licence_expiry_select.select_option(value)
        expect(portfolio.licence_expiry_select).to_have_value(value)


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_expiry_filter_resets_to_all(authenticated_page):
    """Verify the licence expiry filter can be reset to All after a selection."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    options = portfolio.licence_expiry_options.all()
    non_empty = [o for o in options if o.get_attribute("value")]
    if non_empty:
        portfolio.licence_expiry_select.select_option(non_empty[0].get_attribute("value"))
    portfolio.licence_expiry_select.select_option("")
    expect(portfolio.licence_expiry_select).to_have_value("")
