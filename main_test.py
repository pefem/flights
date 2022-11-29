import unittest
import requests


class FlightTest(unittest.TestCase):

    api_url = "http://127.0.0.1:5000/"
    airports_url = f"{api_url}/airports"
    origin = "LHR"
    dest = "BHD"
    date = "28-11-2022"
    flights_url = f"{api_url}/travel/{origin}/{dest}/{date}"

    def test_index(self):
        response = requests.get(FlightTest.api_url)
        self.assertEqual(response.status_code, 200)

    def test_get_airports(self):
        response = requests.get(FlightTest.airports_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)
    
    def test_get_flights(self):
        response = requests.get(FlightTest.flights_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)


if __name__ == "__main__":
    unittest.main()