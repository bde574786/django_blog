from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def signup(request):
    return render(request, 'blog/signup.html')

def blog_view(reqeust):
    return render(reqeust, 'blog/blog_view.html')