"""
Exports page tests.

Route: /exports
Coverage:
  - Export Portfolio button is visible
  - Clicking Export Portfolio button triggers the export action
"""

import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.export_page import ExportPage


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def export_page(authenticated_page):
    """Navigate to the exports page before each test."""
    page = ExportPage(authenticated_page)
    page.navigate()
    return page


# ---------------------------------------------------------------------------
# Page load
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.exports
def test_export_button_visible(export_page):
    """Export Portfolio button is visible on the exports page."""
    expect(export_page.export_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.exports
def test_export_button_enabled(export_page):
    """Export Portfolio button is enabled and ready to interact with."""
    expect(export_page.export_button).to_be_enabled()


# ---------------------------------------------------------------------------
# Export action
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.exports
def test_export_button_click(export_page):
    """Clicking Export Portfolio button does not navigate away from the page."""
    export_page.export_button.click()
    export_page.page.wait_for_load_state("networkidle")
    expect(export_page.export_button).to_be_visible()
