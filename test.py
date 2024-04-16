import datetime

import yagmail
import pandas as pd
from main import NewsFeed
from datetime import date, timedelta
import schedule
import time


def send_email():
    news = NewsFeed(interest=row['interest'], language='en', from_date=yesterdays_date, to_date=todays_date)
    email = yagmail.SMTP(user="@gmail.com", password="iqgk hixs ugao uqwx")
    email.send(
        to=row['email'],
        subject="Yagmail test with attachment",
        contents=f"Hello {row['name']} welcome to your daily news \n" \
                 f"{news.get()}"

    )


while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 15:

        todays_date = date.today()
        yesterdays_date = todays_date - timedelta(days= 1)
        df = pd.read_excel('python.xlsx')
        for index, row in df.iterrows():

            send_email()
    time.sleep(60)
