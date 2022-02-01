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
    user_name = "email goes here"
    message['from'] = user_name
    password = "password goes here"