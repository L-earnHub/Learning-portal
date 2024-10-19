import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import secrets

def generate_otp(): 
    return secrets.randbelow(999999 - 600000 + 1) + 600000

def sendEmailCC(email, otp):
    SMTP_EMAIL = "smtp.gmail.com"
    EMAIL_PORT = 587
    sender_email = "asvaskamal@gmail.com"
    sender_password = "ioivyjshzyscmdnr"
    with smtplib.SMTP(host=SMTP_EMAIL, port=EMAIL_PORT) as s:
        s.starttls()
        s.login(sender_email, sender_password)
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = 'Your OTP code'
        html = f"Your OTP is: {otp}. Please use this to complete the login process."
        message.attach(MIMEText(html, 'plain'))
        s.send_message(message)
        s.quit()


