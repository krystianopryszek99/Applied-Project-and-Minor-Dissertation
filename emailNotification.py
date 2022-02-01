# Script for sending email notification to students after they fill out health check form 

from http import server
import smtplib
from email.message import EmailMessage

def email_notification(to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to
    message

    # Define user and password
    user_name = "gmit.management@gmail.com"
    message['from'] = user_name
    password = "yizzgiyvsvhtxkbw"

    # Server parameters
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user_name, password)
    server.send_message(message)
    server.quit()

    # Define: who the email is send to, subject of the email and the body
    receiver_email = "G00723284@gmail.com"
    subject_of_the_email = "GMIT - Health Check Form"
    email_body = "Dear Student\n\n Thank you for completing the health check form!\n\n\n GMIT - Galway-Mayo Institute Of Technology"
    print("Email has been sent!")
    email_notification(receiver_email, subject_of_the_email, email_body)