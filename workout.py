import datetime
import requests

NUTRI_APP_ID = "APP ID"
NUTRI_API_KEY = "KEY"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = "SHEET LINK"

nutri_header = {"x-app-id":NUTRI_APP_ID, "x-app-key":NUTRI_API_KEY}
query = input("Describe your excercise : ")
params = {
    "query":query,
    "weight_kg":64,
    "height_cm":173.5,
    "age":19
}

response = requests.post(url=NUTRI_ENDPOINT, json=params, headers=nutri_header)
data = response.json()
print(data)

date = datetime.datetime.strftime(datetime.datetime.now(), "%D")
time = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")
to_post = {
    "sheet1":{
        "date":str(date),
        "time":str(time),
        "excercise":data["exercises"][0]["name"],
        "duration":data["exercises"][0]["duration_min"],
        "calories":data["exercises"][0]["nf_calories"]
    }
}

response2 = requests.post(url=SHEET_ENDPOINT, json=to_post)
print(response2.text)