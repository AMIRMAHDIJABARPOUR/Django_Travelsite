from django.shortcuts import render

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        massage = f"You are already logged in{request.user.username}"
    else:
        massage = f"You are not logged in"
    context = {'massage': massage}
    return render(request,"accounts/login.html",context)