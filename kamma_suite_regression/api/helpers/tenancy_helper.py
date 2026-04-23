from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class TenancyHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.tenancies_endpoint = "/v3/tenancies"
        self.tenancy_endpoint = "/v3/tenancies/{kamma_id}"

    def create_tenancy(self, payload, expected_status_code=201):
        return self.api.post(self.tenancies_endpoint, data=payload, expected_status_code=expected_status_code)

    def get_all_tenancies(self, expected_status_code=200):
        return self.api.get(self.tenancies_endpoint, expected_status_code=expected_status_code)

    def get_tenancy_by_id(self, kamma_id, expected_status_code=200):
        return self.api.get(
            self.tenancy_endpoint.format(kamma_id=kamma_id),
            expected_status_code=expected_status_code,
        )

    def update_tenancy(self, kamma_id, payload, expected_status_code=200):
        return self.api.patch(
            self.tenancy_endpoint.format(kamma_id=kamma_id),
            data=payload,
            expected_status_code=expected_status_code,
        )

    def delete_tenancy(self, kamma_id, expected_status_code=200):
        return self.api.delete(
            self.tenancy_endpoint.format(kamma_id=kamma_id),
            expected_status_code=expected_status_code,
        )
