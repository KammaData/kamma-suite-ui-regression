import json
import logging
import os

import requests

from kamma_suite_regression.request_utility.api_env_variables import API_V3

logger = logging.getLogger(__name__)


class RequestException(Exception):
    pass


class ApiV3RequestUtility:
    """
    Token-based HTTP client for the Kamma API v3 service.

    Uses X-SSO-API-Key + X-SSO-Group-ID headers sourced from env vars.
    Exposes the same get/post/patch/put/delete interface as SuiteRequestUtility
    so helpers work with either client.
    """

    def __init__(self, env: str = None):
        env = env or os.environ.get("ENV", "testing")
        config = API_V3[env]
        self.base_url = config["base_url"]
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-SSO-API-Key": os.environ.get(config["api_token"], ""),
            "X-SSO-Group-ID": os.environ.get(config["group_id"], ""),
        }
        self.status_code: int = 0
        self.response_json: dict | list | None = None

    def _handle_response(self, response, expected_status_code):
        self.status_code = response.status_code

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
        response = requests.get(self.base_url + endpoint, params=params, headers=headers or self.headers)
        return self._handle_response(response, expected_status_code)

    def post(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = requests.post(self.base_url + endpoint, json=data, headers=headers or self.headers)
        return self._handle_response(response, expected_status_code)

    def patch(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = requests.patch(self.base_url + endpoint, json=data, headers=headers or self.headers)
        return self._handle_response(response, expected_status_code)

    def put(self, endpoint: str, data: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = requests.put(self.base_url + endpoint, json=data, headers=headers or self.headers)
        return self._handle_response(response, expected_status_code)

    def delete(self, endpoint: str, params: dict = None, headers: dict = None, expected_status_code: int = 200):
        response = requests.delete(self.base_url + endpoint, params=params, headers=headers or self.headers)
        return self._handle_response(response, expected_status_code)
