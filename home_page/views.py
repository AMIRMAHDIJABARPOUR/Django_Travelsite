from django.shortcuts import render

# Create your views here.
def home_main_page(request):
    return render(request,'blog/blog-home.html')