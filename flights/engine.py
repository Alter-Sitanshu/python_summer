import requests
import os

FLIGHT_API = "https://test.api.amadeus.com/v2/shopping/flight-offers"
CODE_API = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_API_KEY = os.environ.get("FLIGHT_KEY")

class FlightSearch:
    def __init__(self) -> None:
        self.token = self.getToken()
        self.header = {
            "Authorization": f"Bearer {self.token}"
        }
    def getToken(self) -> str:
        auth_params = {
            "grant_type":"client_credentials",
            "client_id": FLIGHT_API_KEY,
            "client_secret":os.environ.get("FLIGHT_SECRET")
        }
        auth_head = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        auth = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", data=auth_params, headers=auth_head)
        return auth.json()['access_token']
    def initialise(self, loc: str, des: str, depart: str, adults: int) -> dict:
        params = {
            "originLocationCode":loc,
            "destinationLocationCode":des,
            "departureDate":depart,
            "adults":adults,
            "currencyCode":"INR" #specified due according to the region
        }
        return params
    
    def flightSearch(self, params: dict):
        response = requests.get(url=FLIGHT_API, params=params, headers=self.header)
        filtered_search = list(response.json()['data'])
        price_list = [eval(i["price"]["total"]) for i in filtered_search]
        return price_list
    def getCode(self, keyword: str) -> str:
        response_code = requests.get(url=CODE_API, params={"countryCode":"IN", "keyword": keyword, "max":1}, headers=self.header)
        return response_code.json()["data"][0]["iataCode"]


