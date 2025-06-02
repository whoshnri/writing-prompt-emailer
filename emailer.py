# this file contails the email automation

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
load_dotenv()
from prompt import chat
import time
import pandas as pd

prompt = "Give me a single idea for an article or an essay i can write to improve my writing skills and develop a habit."

# body = chat(prompt)
sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body, cc='blank?'):
    current_date = time.strftime("%d-%m-%Y")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject + current_date
    if cc != 'blank?':
        msg['Cc'] = cc

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        log_prompt(body,'Successful')
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        log_prompt(body,'Failed')

# send_email("henrybassey2007@gmail.com","Article Idea | Daily tasks" , body)

def log_prompt(body, status):
    current_date = time.strftime("%d-%m-%Y")
    log = pd.read_csv('logs.csv')
    new_entry = {"Date": current_date, "Topic": body , "Status" : status}
    log = pd.concat([log, pd.DataFrame([new_entry])], ignore_index=True)
    log.to_csv('logs.csv', index=False)
    
send_email('henrybassey2007@gmail.com',"Test2 | With logs " , 'This is another test but it logs thigs into the csv file now')
