from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class PropertiesHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.properties_endpoint = "/v3/properties"
        self.property_endpoint = "/v3/properties/{kamma_id}"

    def get_property(self, kamma_id, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.get(
            self.property_endpoint.format(kamma_id=kamma_id),
            params=params,
            expected_status_code=expected_status_code,
        )

    def create_property(self, payload, expected_status_code=201):
        return self.api.post(self.properties_endpoint, data=payload, expected_status_code=expected_status_code)

    def update_property(self, kamma_id, payload, expected_status_code=200):
        return self.api.patch(
            self.property_endpoint.format(kamma_id=kamma_id),
            data=payload,
            expected_status_code=expected_status_code,
        )

    def delete_property(self, kamma_id, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.delete(
            self.property_endpoint.format(kamma_id=kamma_id),
            params=params,
            expected_status_code=expected_status_code,
        )
