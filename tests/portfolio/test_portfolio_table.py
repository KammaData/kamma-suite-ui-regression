"""
Portfolio table tests.

Route: /portfolio
Coverage:
  - All column headers are visible
  - Table renders at least one row
  - Current Schemes column contains only valid badge values
  - Licence Required column contains only valid badge values
  - Upcoming Licence Required column contains only valid badge values
  - Compliance Status column contains only valid values
"""

import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.portfolio_page import PortfolioPage

VALID_SCHEME_VALUES = {"Mandatory", "Additional", "Selective", "Unknown", "-"}
VALID_LICENCE_REQUIRED_VALUES = {"Mandatory", "Additional", "Selective", "Unknown", "None", "Indeterminate"}
VALID_UPCOMING_LICENCE_VALUES = {"Mandatory", "Additional", "Selective", "Unknown", "None", "Indeterminate"}
VALID_COMPLIANCE_STATUS_VALUES = {"Non-compliant", "Compliant"}


# --- Column header tests ---

@pytest.mark.smoke
@pytest.mark.dashboard
def test_portfolio_table_visible(authenticated_page):
    """Verify the properties table is rendered on the portfolio page."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.table).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_table_has_rows(authenticated_page):
    """Verify the properties table contains at least one row."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    assert portfolio.table_rows.count() > 0


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_id_visible(authenticated_page):
    """Verify the ID column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_id).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_address_visible(authenticated_page):
    """Verify the Address column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_address).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_authority_visible(authenticated_page):
    """Verify the Local Authority column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_authority).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_schemes_visible(authenticated_page):
    """Verify the Current Schemes column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_schemes).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_licence_required_visible(authenticated_page):
    """Verify the Licence Required column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_licence_required).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_upcoming_licence_visible(authenticated_page):
    """Verify the Upcoming Licence Required column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_upcoming_licence).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_people_visible(authenticated_page):
    """Verify the People column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_people).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_households_visible(authenticated_page):
    """Verify the Households column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_households).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_compliance_status_visible(authenticated_page):
    """Verify the Compliance Status column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_compliance_status).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_col_header_actions_visible(authenticated_page):
    """Verify the Actions column header is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.col_header_actions).to_be_visible()


# --- Column value validation tests ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_schemes_column_contains_valid_values(authenticated_page):
    """Verify every badge in the Current Schemes column is a recognised scheme type."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    cells = portfolio.cells_schemes.all()
    for cell in cells:
        badges = cell.locator("span.fi-badge span.grid span").all()
        for badge in badges:
            value = badge.inner_text().strip()
            assert value in VALID_SCHEME_VALUES, f"Unexpected scheme value: '{value}'"


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_licence_required_column_contains_valid_values(authenticated_page):
    """Verify every badge in the Licence Required column is a recognised value."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    cells = portfolio.cells_licence_required.all()
    for cell in cells:
        badges = cell.locator("span.fi-badge span.grid span").all()
        for badge in badges:
            value = badge.inner_text().strip()
            assert value in VALID_LICENCE_REQUIRED_VALUES, f"Unexpected licence required value: '{value}'"


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_upcoming_licence_column_contains_valid_values(authenticated_page):
    """Verify every badge in the Upcoming Licence Required column is a recognised value."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    cells = portfolio.cells_upcoming_licence.all()
    for cell in cells:
        badges = cell.locator("span.fi-badge span.grid span").all()
        for badge in badges:
            value = badge.inner_text().strip()
            assert value in VALID_UPCOMING_LICENCE_VALUES, f"Unexpected upcoming licence value: '{value}'"


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_status_column_contains_valid_values(authenticated_page):
    """Verify every value in the Compliance Status column is compliant or non-compliant."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    cells = portfolio.cells_compliance_status.all()
    for cell in cells:
        value = cell.locator("span.fi-badge").inner_text().strip()
        assert value in VALID_COMPLIANCE_STATUS_VALUES, f"Unexpected compliance status: '{value}'"


# --- Row interaction tests ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_table_row_links_to_property(authenticated_page, base_url):
    """Verify each table row links to a property detail page."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    first_link = portfolio.table_rows.first.locator("a.fi-ta-col").first
    href = first_link.get_attribute("href")
    assert href and "/portfolio/" in href


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_table_row_actions_menu_opens(authenticated_page):
    """Verify the actions menu on the first table row can be opened."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    actions_btn = portfolio.table_rows.first.locator("button[aria-label='Actions']")
    actions_btn.click()
    expect(portfolio.table_rows.first.locator(".fi-dropdown-panel")).to_be_visible()
