from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class RoomSizeHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.room_size_endpoint = "/v3/room-sizes/{place_id}"

    def get_room_size(self, place_id, expected_status_code=200):
        return self.api.get(
            self.room_size_endpoint.format(place_id=place_id),
            expected_status_code=expected_status_code,
        )
