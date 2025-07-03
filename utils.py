import requests
from .models import Article


def get_news_from_api(url):
try:
    data = requests.get(url)
    data= data.json()
    if data.get('article'):
        for articles in data.get('article')
        source = article.get('source').get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
         url =article.get('url')
         urlToImage =article.get('urlToImage')
         publishedAt = article.get('publishedAt')
         content = article.get('content')

         Article.obeject.create(
            source = source
            author = author
            title = title
            description = description
             url = url
         urlToImage = urlToImage
         publishedAt = publishedAt
         content = content
         )

    except Exception as e:
        print(e)