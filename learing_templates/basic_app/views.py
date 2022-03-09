from django.shortcuts import render

# Create your views here.


def welcome(request):
    text_dict = {"text":"hello world","number":1000}
    return render(request,"basic_app\welcome_page.html",text_dict)

def other(request):
    return render(request,"basic_app\other_page.html")

def relative(request):
    return render(request,"basic_app\\relative_url_page.html")

def base(request):
    return render(request,"basic_app\\base.html")