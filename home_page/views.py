from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactModelForm, NewsletterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home_main_page(request):
    return render(request, "webpage/index.html")


def about_page(request):
    return render(request, "webpage/about.html")


def elements(request):
    return render(request, "webpage/elements.html")


def contact(request):
    if request.method == "POST":

        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent.")
            form = ContactModelForm()
        else:
            messages.error(request, "Please enter your message.")
    else:
        form = ContactModelForm()
    context = {"form": form}
    return render(request, "webpage/contact.html", context)


def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your email has been sent.")
            next_url = request.POST.get("next", "/")
            return redirect(next_url)
        else:
            # فرم POST بود ولی نامعتبر، دوباره همون صفحه
            messages.error(request, "Please enter a valid email.")
            next_url = request.POST.get("next", "/")
            return redirect(next_url)

    return render(request, "webpage/index.html")
