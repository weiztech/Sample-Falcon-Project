from common.base_tests import BaseTest


class PassengerAppTests(BaseTest):
    '''
    Passengers Apps on `API` level
    '''

    def test_api_results(self):
        # Make sure the API return expected output
        # Case 1
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 3]],
            "ttl_passenger": 30
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.json,
            [[[19, 25, 1], [2, 26, 27, 3], [4, 5], [6, 28, 20]],
             [[21, 29, 7], [8, 30, '', 9], [10, 11], [12, '', 22]],
             [[], [13, '', '', 14], [15, 16], [17, '', 23]],
             [[], [], [], [18, '', 24]]])

        # Case 2
        data = {
            "seats": [[1, 1], [3, 5], [2, 1], [2, 1]],
            "ttl_passenger": 10
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.json,
            [[[9], [1, '', '', '', 2], [3], [10]],
             [[], [4, '', '', '', 5], [6], ['']],
             [[], [7, '', '', '', 8], [], []]])

        # Case 3
        data = {
            "seats": [[1, 1], [3, 5], [2, 1], [2, 1]],
            "ttl_passenger": 20
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.json,
            [[[9], [1, 12, 13, 14, 2], [3], [10]],
             [[], [4, 15, 16, 17, 5], [6], [11]],
             [[], [7, 18, 19, 20, 8], [], []]])

    def test_api_validation(self):
        # Test Api input validation

        # return status code 400 if ttl passenger greater than max seats
        # available seats: 30, ttl passenger: 350
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 3]],
            "ttl_passenger": 350
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # return status code 400 if ttl passenger lower or equal to zero
        # Case 1: ttl passenger -1
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 3]],
            "ttl_passenger": -1
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # Case 2: ttl passenger 0
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 3]],
            "ttl_passenger": 0
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # return status code 400 if `seats`/ not 2D array
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 3, 1]],
            "ttl_passenger": -1
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # return status code 400 if `seats`/ 2D array contain zero
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 0]],
            "ttl_passenger": -1
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # return status code 400 if `seats`/ 2D array contain zero
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, 0]],
            "ttl_passenger": -1
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)

        # return status code 400 if `seats`/ 2D array contain not an integer
        data = {
            "seats": [[2, 3], [3, 4], [3, 2], [4, "Yay"]],
            "ttl_passenger": -1
        }

        result = self.simulate_post(
            '/', headers={"content-type": "application/json"}, json=data)
        self.assertEqual(
            result.status_code, 400)
