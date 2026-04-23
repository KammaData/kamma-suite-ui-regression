import json
import logging
import os
from playwright.sync_api import APIRequestContext

logger = logging.getLogger(__name__)


class RequestException(Exception):
    """Raised when an API response status code does not match expectations."""

    pass


class SuiteRequestUtility:
    """
    Thin wrapper around Playwright's APIRequestContext.

    Uses the authenticated browser session (via storage state) so API calls
    share the same credentials as the browser under test.

    Usage in a test:
        def test_something(authenticated_request):
            api = SuiteRequestUtility(authenticated_request)
            data = api.get("/api/v1/properties")
            assert data["total"] > 0
    """

    def __init__(self, request_context: APIRequestContext):
        self.context = request_context
        self.group_id = os.environ.get("KAMMA_PS_API_GROUP_ID", "")
        self.status_code: int = 0
        self.response_json: dict | list | None = None

    def _with_group(self, params: dict = None) -> dict:
        return {**(params or {}), "_sg": self.group_id}

    def _handle_response(self, response, expected_status_code):
        self.status_code = response.status

        try:
            self.response_json = response.json()
        except Exception:
            self.response_json = None

        expected_codes = (
            list(expected_status_code)
            if isinstance(expected_status_code, (list, tuple))
            else [expected_status_code]
        )

        if self.status_code not in expected_codes:
            expected_str = str(expected_codes[0]) if len(expected_codes) == 1 else f"one of {expected_codes}"
            raise RequestException(
                f"Incorrect status code. Expected {expected_str}, "
                f"Actual: {self.status_code}, URL: {response.url}, "
                f"Response: {json.dumps(self.response_json, default=str)}"
            )

        logger.debug(f"{response.request.method} {response.url} -> {self.status_code}")
        return self.response_json

    def get(self, endpoint: str, params: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = self.context.get(endpoint, params=self._with_group(params), headers=headers)
        return self._handle_response(response, expected_status_code)

    def post(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = self.context.post(endpoint, data=json.dumps(data), params=self._with_group(), headers=headers)
        return self._handle_response(response, expected_status_code)

    def patch(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = self.context.patch(endpoint, data=json.dumps(data), params=self._with_group(), headers=headers)
        return self._handle_response(response, expected_status_code)

    def put(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = self.context.put(endpoint, data=json.dumps(data), params=self._with_group(), headers=headers)
        return self._handle_response(response, expected_status_code)

    def delete(self, endpoint: str, params: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = self.context.delete(endpoint, params=self._with_group(params), headers=headers)
        return self._handle_response(response, expected_status_code)
