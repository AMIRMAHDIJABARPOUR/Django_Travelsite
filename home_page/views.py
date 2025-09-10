from django.shortcuts import render

# Create your views here.
def home_main_page(request):
    return render(request,'webpage/index.html')
def about_page(request):
    return render(request,'webpage/about.html')
def elements(request):
    return render(request,'webpage/elements.html')
def contact(request):
    return render(request,'webpage/contact.html')