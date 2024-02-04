import pandas as pd
import smtplib, ssl
import numpy as np

import os
from dotenv import load_dotenv

from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

#ENVIRONMENT VARIABLES
path = os.getenv("excel_path")
sender = os.getenv("sender")
receiver = os.getenv("receiver")
password = os.getenv("temp_pwd")
#----------------------------


df = pd.read_excel(path)
today = date.today()

def get_today_birthday(date,calendar):
    day = date.day - 1
    month = date.month
    return calendar[month][day]

def send_email(birthday_name, recipient, receiver, password):
    
    #SSL CONFIG
    port = 465
    context = ssl.create_default_context()
    #----------------------

    #Initialize sender and message
    sender_email = recipient
    receiver_email = receiver
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cumple de " + str(birthday_name)
    message["From"] = sender_email
    message["To"] = receiver_email
    #------------------------------------------------------
    
    # Create the plain-text and HTML version of your message
    html = """\
    <html>
    <body>
        <p>Hola<br><br>Hoy es el cumple de <b>""" + str(birthday_name) + """</b><br><br>Felicitalo!
        </p>
    </body>
    </html>
    """
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(recipient, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        
def verify_birthday(birthday_name):
    try:
        return np.isnan(birthday_name)
    except:
        return False

if __name__ == "__main__":
    birthday_name = get_today_birthday(today, df)
    if(verify_birthday):
        send_email(birthday_name,sender,receiver,password)
    
    



