# Script for sending email notification to students after they fill out health check form 

import smtplib
from email.message import EmailMessage

def email_notification(to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to
    message

    # Message body
    message.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <p style="color:Black; font-family:Helvetica;">
                Dear Student,
                <br><br>
                <b>Thanks for the registration!</b>
                <br><br>
                Your account is now successfully created. You now have access to check in!
                <br>
                All your information is being stored securly on the database.
                <br><br><br>
                <img src="https://cualliance.ie/wp-content/uploads/2020/04/logo-1-copy.png" alt="Gmit Logo" width="398" height="78">
                <br><br>
                GMIT - Galway-Mayo Institute Of Technology
                <br>
                More on Covid-19: Covidofficer@gmit.ie
                <br>
                Visit Us: https://www.gmit.ie/
            </p>
        </body>
    </html>
    """, subtype='html')

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

# Sends email when called
def sendNotification(email_var):
    # Define: who the email is send to, subject of the email and the body
    receiver_email = email_var.get()
    subject_of_the_email = "CMS - Registration"
    # Email body is defined but no content is passed in, uses HTML to print the content of the body
    email_body = ""
    print("Email has been sent!")
    email_notification(receiver_email, subject_of_the_email, email_body)