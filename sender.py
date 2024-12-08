#!/usr/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_email(sender_user, sender_password, recipient_email, subject, html_file):
    with open(html_file, 'r') as f:
        html_body = f.read()

    with open(plain_text_file, 'r') as f:
        plain_text_body = f.read()

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email
    message['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

    html_part = MIMEText(html_body, "html")
    plain_text_part = MIMEText(plain_text_body, "plain")

    message.attach(plain_text_part)
    message.attach(html_part)

    # SMTP details here:
    with smtplib.SMTP_SSL("smtp.hatters.org.uk", 465) as smtp:
        smtp.login(sender_user, sender_password)
        smtp.sendmail(sender_user, recipient_email, message.as_string())

# Replace with SMTP auth credentials and email contents
sender_email = "Chrystal Baker-Bates <chrystal@bakerbates.com>"
sender_user = "USERNAME"
sender_password = "PASSWORD"
subject = "Test // Happy Christmas 2024 // Test"
html_file = "2024/version-d.html"
plain_text_file = "2024/text.txt"

# Read recipient addresses from a file
with open('recipient_addresses.txt', 'r') as f:
    for recipient_email in f:
        recipient_email = recipient_email.strip()  # Remove newline characters
        send_email(sender_user, sender_password, recipient_email, subject, html_file)