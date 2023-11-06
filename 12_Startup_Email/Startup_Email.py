#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def send_email(sender_email, sender_password, receiver_email):
    # Get the location of the device
    location = get_location()

    # Compose the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Device Location'

    body = f"Hi,\n\nMy device is currently online and its location is:\n\n{location}\n\n انا شمشون الجبار .... انا مخترع الممبار"

    message.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

def get_location():
    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        location = data['loc']
        return location
    except Exception as e:
        return "Location could not be retrieved."

# Usage
sender_email = 'omar.saudiyw@gmail.com'  # Your email address
sender_password = 'egwcekfbsccqyefj'  # Your email password
receiver_email = 'sweta3gta5@gmail.com'  # Your friend's email address

send_email(sender_email, sender_password, receiver_email)