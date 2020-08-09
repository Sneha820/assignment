from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Welcome Bhavaikya</h1>")

def home(request):
    return render(request,"base.html")

def comment(request):
    return render(request,"myapp/comment.html")

def blog(request):
    return render(request,"myapp/blog.html")