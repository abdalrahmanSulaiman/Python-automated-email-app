#api key = bdb7b0a9c1d04865bce5f5f903b20c87
import requests
from pprint import pprint
import yagmail
import pandas as pd
class NewsFeed:
    base_url = f'https://newsapi.org/v2/everything?'
    def __init__(self,interest,language,from_date,to_date):
        self.interest = interest
        self.language = language
        self.from_date = from_date
        self.to_date = to_date

    def  get(self):

        full_url = self._build_url()

        data = requests.get(full_url)
        content = data.json()
        titles_set = []
        urls_set = []
        news_string = ""


        for i in range (len(content['articles'])):
            title = content['articles'][i]['title']
            titles_set.append(title)
        for x in range (len(content['articles'])):
            url = content['articles'][x]['url']
            urls_set.append(url)
        for z in range (len(content['articles'])):
            news_string += f"{titles_set[z]} \n" \
                           f"{urls_set[z]}\n\n"
        return news_string

    def _build_url(self):
        full_url = self.base_url + f"qInTitle={self.interest}" + \
                   f"&from={self.from_date}" + \
                   f"&to={self.to_date}" + \
                   f"&language={self.language}" + \
                   f"&apiKey=bdb7b0a9c1d04865bce5f5f903b20c87"
        return full_url


if __name__ == '__main__':
    df = pd.read_excel('python.xlsx')
    for index, row in df.iterrows():
        news = NewsFeed(interest=row['interest'], language='en', from_date=2023 - 7 - 30, to_date=2023 - 7 - 31)
        receiver = row['email']
        body = f"Hello {row['name']} welcome to your daily news" \
               f"{news.get()}"

        email = yagmail.SMTP(user="pythontest321456@gmail.com", password="iqgk hixs ugao uqwx")
        email.send(
            to=receiver,
            subject="Yagmail test with attachment",
            contents=body

        )







