from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class LicenceHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.licences_endpoint = "/v3/licences"
        self.licence_endpoint = "/v3/licences/{licence_id}"
        self.licence_upload_endpoint = "/v3/licences/{licence_id}/upload"
        self.licence_download_endpoint = "/v3/licences/{licence_id}/download"
        self.licence_file_endpoint = "/v3/licences/{licence_id}/file"

    def create_licence(self, payload, expected_status_code=201):
        return self.api.post(self.licences_endpoint, data=payload, expected_status_code=expected_status_code)

    def get_licence(self, licence_id, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.get(
            self.licence_endpoint.format(licence_id=licence_id),
            params=params,
            expected_status_code=expected_status_code,
        )

    def update_licence(self, licence_id, payload, expected_status_code=200):
        return self.api.patch(
            self.licence_endpoint.format(licence_id=licence_id),
            data=payload,
            expected_status_code=expected_status_code,
        )

    def delete_licence(self, licence_id, expected_status_code=200):
        return self.api.delete(
            self.licence_endpoint.format(licence_id=licence_id),
            expected_status_code=expected_status_code,
        )

    def delete_licence_file(self, licence_id, expected_status_code=200):
        return self.api.delete(
            self.licence_file_endpoint.format(licence_id=licence_id),
            expected_status_code=expected_status_code,
        )
