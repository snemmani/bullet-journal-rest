from django.shortcuts import render, redirect

def index(request):
    print(request)
    user = request.user
    print(user)
    if user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
