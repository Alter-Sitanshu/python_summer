import requests
import engine
import os

SHEET_API = "https://api.sheety.co/b598c6c75b4ad2812c567fa8c1f6c2f0/flightFinder/loc"
USER_API = "https://api.sheety.co/b598c6c75b4ad2812c567fa8c1f6c2f0/flightFinder/user"
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

#----user manager---------
def addUser(name: str, email: str):
    user_response = requests.post(url=USER_API, json={"user":{"name":name.title(), "email":email}}, headers=SHEET_HEAD)
    print(user_response.text)

def getUser(name: str) -> dict[str, str]:
    user_response = requests.get(url=USER_API, headers=SHEET_HEAD)
    user_id = {i["name"]:i["email"] for i in user_response.json()["user"] if i["name"] == name.title()}
    return user_id

def deleteUser(id: int):
    user_response = requests.delete(url=f"{USER_API}/{id}", headers=SHEET_HEAD)
    print(user_response.text)