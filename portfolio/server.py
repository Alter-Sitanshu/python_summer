from flask import Flask, render_template, request
import smtplib
import os

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
    mail_address = request.form.get('Email')
    message = request.form.get('message')
    connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=f"Subject: New Connewction\n\n{mail_address}\n\n{message}" )
    return render_template('index.html')


if __name__ == "__main__":
        app.run(debug=True)
