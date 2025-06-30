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

def send_email(mail_address, message):
    """Function to send email - creates connection each time"""
    try:
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=SENDER, password=PASS)
        
        msg = MIMEMultipart()
        msg["From"] = SENDER
        msg["To"] = RECEIVER
        msg["Subject"] = Header("New Connection request")
        msg.attach(MIMEText(f"From: {mail_address}\n\nMessage:\n{message}", "plain", "utf-8"))
        
        connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=msg.as_string())
        connection.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def home_render():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def handle_submit():
    mail_address = request.form.get('Email')
    message = request.form.get('message')
    
    if send_email(mail_address, message):
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
        app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
