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
                <img src="https://upload.wikimedia.org/wikipedia/en/2/28/ATU-Logo-Full-RGB-Teal.png" alt="Gmit Logo" width="398" height="78">
                <br><br>
                ATU - Atlantic Technological University
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
def sendNotification(name):
    # Define: who the email is send to, subject of the email and the body
    receiver_email = name.get() + "@gmit.ie"
    subject_of_the_email = "CMS - Registration"
    # Email body is defined but no content is passed in, uses HTML to print the content of the body
    email_body = ""
    print("Email has been sent to: " + name.get() + "@gmit.ie\n")
    email_notification(receiver_email, subject_of_the_email, email_body)