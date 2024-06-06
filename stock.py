import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


stock_api_key = "API KEY"
news_api_key = "API KEY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

sender = "SENDER MAIL_ID"
app_pass = "KEY"


date = str((datetime.datetime.now() - datetime.timedelta(days=1)).date())
yesterday = str((datetime.datetime.now() - datetime.timedelta(days=2)).date())

stock_fetch = requests.get(url=STOCK_ENDPOINT, params={"function":"TIME_SERIES_DAILY", "symbol":STOCK, "apikey":stock_api_key})
stock_data: tuple = (float(stock_fetch.json()['Time Series (Daily)'][date]["4. close"]),float(stock_fetch.json()['Time Series (Daily)'][yesterday]["4. close"]))

margin = ((stock_data[0]-stock_data[1])/stock_data[0])*100
if abs(margin) > 5:
    news_fetch = requests.get(url=NEWS_ENDPOINT, params={"q":"tesla", "from":date, "sortBy":"published", "apiKey":news_api_key})
    articles = news_fetch.json()["articles"][:3]
    news: dict[str, str] = {blog["title"]:blog["description"] for blog in articles}
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = "RECEIVER MAIL ID"
    if margin>0: 
        msg["Subject"]= Header(f"TSLA: 🔺{margin: .2f}%\n", "utf-8")
    else:
        msg["Subject"]= Header(f"TSLA: 🔻{abs(margin): .2f}%\n")
    mail_text = ""
    for blog in news:
        mail_text += f"Headline :{blog}\nDescription :{news[blog]}\n\n"
    msg.attach(MIMEText(mail_text, "plain", "utf-8"))
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender, password=app_pass)
        connection.sendmail(from_addr=sender, to_addrs="RECEIVER MAIL ID", msg=msg.as_string() )


