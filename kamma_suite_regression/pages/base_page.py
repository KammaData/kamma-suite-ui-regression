import os
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._group_id = os.environ.get("KAMMA_PS_API_GROUP_ID", "")

    def navigate(self, path: str = "/"):
        if self._group_id:
            separator = "&" if "?" in path else "?"
            url = f"{path}{separator}_sg={self._group_id}"
        else:
            url = path
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for_network_idle(self):
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def assert_snapshot(self, name: str, assert_snapshot_fn, full_page: bool = False):
        """Compare a screenshot against the stored baseline using pixel diffing."""
        assert_snapshot_fn(self.page.screenshot(full_page=full_page), name=f"{name}.png")
