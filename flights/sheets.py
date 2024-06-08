import requests
import engine
import os

SHEET_API = "https://api.sheety.co/b598c6c75b4ad2812c567fa8c1f6c2f0/flightFinder/loc"
SHEET_HEAD = {
    "Authorization": f"Bearer {os.environ.get("FLIGHT_SHEET")}"
}
def insert():
    customer = engine.FlightSearch()
    city = input("Enter City initials : ").upper()
    iata_code = customer.getCode(keyword=city)
    min_price = input("Enter the min price for flight(INR) : ")
    to_post = {
        "loc":{
            "location":str(iata_code),
            "price":int(min_price)
        }
    }
    sheet_response = requests.post(url=SHEET_API, json=to_post, headers=SHEET_HEAD)
    print(sheet_response.text)

def deleteRow(index: int):
    sheet_response = requests.delete(url=f"{SHEET_API}/{index}", headers=SHEET_HEAD)
    print(sheet_response.text)
