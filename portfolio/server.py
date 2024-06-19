from flask import Flask, render_template, request
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

RECEIVER = os.environ.get('RECEIVER')
SENDER = os.environ.get('SENDER')
PASS = os.environ.get("APP_PASS")

app = Flask(__name__)
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=SENDER, password=PASS)

@app.route('/')
def home_render():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def handle_submit():
    global connection
    msg = MIMEMultipart()
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    mail_address = request.form.get('Email')
    message = request.form.get('message')
    msg["Subject"]= Header("New Connection request")
    msg.attach(MIMEText(f"{mail_address}\n{message}", "plain", "utf-8"))
    connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=msg.as_string() )
    return render_template('index.html')


if __name__ == "__main__":
        app.run(debug=True)
