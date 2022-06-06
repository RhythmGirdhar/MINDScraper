#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
from bs4 import BeautifulSoup


# In[15]:


url = "https://www.aljazeera.com/where/mozambique/"
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

aljazeera_paper = getHTMLdocument(url)
print(aljazeera_paper)


# In[20]:


base_url = "https://www.aljazeera.com"
soup = BeautifulSoup(aljazeera_paper, 'html.parser')
all_articles = soup.find_all("a", {"class": "u-clickable-card__link"})

article_links = [base_url + article['href'] for article in all_articles]
print(article_links)


# In[48]:


from newspaper import Article
import json
from tqdm import tqdm

article_collections = []

# article_url = article_links[0]
# article = Article(article_url)
# article.download()
# article.parse()
# article_soup = BeautifulSoup(article.html, 'html.parser')
# article_soup.find("p", {"class": "article__subhead"}).find('em').string

for article_url in tqdm(article_links):
    article = Article(article_url)
    article.download()
    article.parse()
    article_soup = BeautifulSoup(article.html, 'html.parser')
    subtitle = ''
    try:
        subtitle =  article_soup.find("p", {"class": "article__subhead"}).find('em').string
    except:
        pass
    article_collections.append(
        { 'title': article.title, 'subtitle': subtitle, 'content': article.text }
    )

# print(len(article_collections))
with open('data.json', 'w') as f:
    json.dump(article_collections, f)

# json.dumps(article_collections)


# In[ ]:




