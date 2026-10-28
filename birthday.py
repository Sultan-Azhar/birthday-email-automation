# import smtplib
# from email.mime.text import MIMEText 
# sender = "sultanazhar.developer786@gmail.com"
# password = "lpk gutj drk zgk"
# # receiver = "geesultan44@gmail.com"
# receiver = input("Enter the receiver's email address: ")
# name = input("Enter the receiver's name: ")
# message = f"Dear {name},\n\nWishing you a very Happy Birthday! May your day be filled with joy, love, and wonderful memories.\n\nBest wishes,\nSultan Azhar"
# message = MIMEText(message)
# message['Subject'] = f"Happy Birthday, {name}!"
# message['From'] = sender
# message['To'] = receiver
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(sender, password)
# server.send_message(message)
# server.quit()

import smtplib 
from email.mime.tex import MiMEText
from datetime import datetime
import time
sender = "sultanazhar.developer786@gmail.com"
password = "lpk gutj drk zgk"
receiver = input("Enter the receiver's email address: ")
name = input("Enter the receiver's name: ")
dob = input("Enter the receiver's date of birth (dd-mm): ")
send_hour = 5
send_minute = 10
while True:
    now = datetime.now()
    today = now.strftime("%d-%m")
    if today == dob and now.hour == send_hour and now.minute == send_minute:
       message = f"Dear {name},\n\nWishing you a very Happy Birthday! May your day be filled with joy, love, and wonderful memories.\n\nBest wishes,\nSultan Azhar"
       message = MIMEText(message)
       message['Subject'] = f"Happy Birthday, {name}!"
       message['From'] = sender
       message['To'] = receiver

       try:
           server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
           server.login(sender, password)
           server.send_message(message)
           server.quit()
           print("Birthday email sent successfully!")
         except Exception as e:
           print(f"Failed to send email: {e}")  
         break
    time.sleep(60)





