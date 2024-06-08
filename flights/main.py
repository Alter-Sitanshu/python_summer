import requests
import engine
import smtplib
import sheets
import os

#---THE SHEETS CONTAINS LOCATION AND MIN PRICE-----
SHEET_API = "https://api.sheety.co/b598c6c75b4ad2812c567fa8c1f6c2f0/flightFinder/loc"
SHEET_HEAD = {
    "Authorization": f"Bearer {os.environ.get("FLIGHT_SHEET")}"
}

sheet_response = requests.get(url=SHEET_API, headers=SHEET_HEAD)
data = sheet_response.json()["loc"]
customer = engine.FlightSearch()
loc = input("DEPARTURE LOCATION IATA CODE : ")
depart = input("Enter dateof departure (YYYY-MM-DD) : ")
adults = int(input("No. of adults : "))

sender = os.environ.get("SENDER")
app_pass = os.environ.get("APP_PASS")
def priceCheck():
    for content in data:
        des = content["location"]
        min_price = content["price"]
        params = customer.initialise(loc=loc, des=des, depart=depart, adults=adults)
        price_list = customer.flightSearch(params=params)
        if min(price_list)<min_price:
            msg = f"Header :DEALS FOUND !!!\n\nDeals available for {des}"
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=sender, password=app_pass)
                connection.sendmail(from_addr=sender, to_addrs=os.environ.get("RECEIVER"), msg=msg )

priceCheck()

#----Can Add a row to the sheet------
#sheets.insert()

#----Can Delete a row by specifying the index-----
#sheets.delete(index)