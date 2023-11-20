from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def news_list(request):
    return render(request, 'main/news_list.html')

def sidebar(request):
    return render(request, 'main/sidebar.html')

def no_page_error(request, exception):
    return render(request, 'main/no_page_error.html', status=404)

def account(request):
    return render(request, 'main/account.html')
