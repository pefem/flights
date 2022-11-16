# getting flight details using origin and destination airports
import requests


class Flights:

    def __init__(self) -> None:
        self.base_url = 'https://www.aerlingus.com/api/v2/flights/fixed'
        self.headers = self.get_headers()

    def get_headers(self):
        return {
                'authority': 'www.aerlingus.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://www.aerlingus.com/html/flightSearchResult.html',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'x-correlation-id': '75914e26-d507-4ef7-9340-3a7969b13086',
            }

    def enter_details(self, origin, destination, date):
        params = {
            'departureDate': date,
            'destination': destination,
            'fare': 'low',
            'numAdults': '1',
            'numChildren': '0',
            'numInfants': '0',
            'numYouths': '0',
            'origin': origin,
        }

        return params
    
    def get_response(self, params):
        response = requests.get(self.base_url, params=params, headers=self.headers)
        return response


