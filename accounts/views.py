from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):

    if request.method =='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'welcome {username}')
                return redirect('/')

    return render(request,"accounts/login.html")

@login_required(login_url='/accounts/login/')
def user_logout(request):
    # if request.user.is_authenticated:  # مطمئن شو کاربر لاگین بوده
    username = request.user.username  # نام کاربری رو قبل از logout ذخیره کن
    logout(request)
    messages.success(request,f'goodbye {username}')
    return redirect('/')
# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password1 = form.cleaned_data.get('password1')
#             password2 = form.cleaned_data.get('password2')
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'username already exists')
#                 return render(request, "accounts/signup.html", {'form': form})
#             if password1 != password2:
#                 messages.error(request,'password dont match')
#                 return render(request, "accounts/signup.html", {'form': form})
#             user=form.save()
#             login(request,user)
#             messages.success(request,f'welcome to our blog{username}')
#             return redirect('/')
#         else:
#             for error in form.non_field_errors():
#                 messages.error(request, error)
#             return render(request, "accounts/signup.html", {'form': form})  # اضافه کردن else برای خطاهای فرم
#     else:
#         form = UserCreationForm()
#     return render(request,"accounts/signup.html")
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return render(request, "accounts/signup.html", {'form': form})
            user = form.save()
            login(request, user)
            messages.success(request, f'welcome to our blog {username}')
            return redirect('/')
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
            return render(request, "accounts/signup.html", {'form': form})
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})
