# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

# res = requests.get('https://www.goodreads.com/quotes', headers=user_agent)

# soup = BeautifulSoup(res.text, 'html.parser')

# quotes = soup.find_all('div', class_="quoteDetails")

# quotes_list = []
# authors_list = []
# likes_list = []

# for quote in quotes:
#     quotes_list.append(quote.find('div').text.split('―')[0].strip().replace('“', '').replace('”', ''))
#     authors_list.append(quote.find('div').text.split('―')[1].strip())
#     likes_list.append(quote.find('div', class_="right").text.strip().split(' ')[0])

# df = pd.DataFrame({'quotes': quotes_list, 'authors': authors_list, 'likes': likes_list})
# df.to_csv('quotes.csv')