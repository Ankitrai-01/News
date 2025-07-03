from django.shortcuts import render

# Create your views here.
def home(request):
   #url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-06-02&sortBy=publishedAt&apiKey=ae36f871eaa34ddf9fa8a42c2d189fe3'
    get_news_from_api(url)
    return render(request , 'home.html' , context = {'article' : Article.objects.all()})