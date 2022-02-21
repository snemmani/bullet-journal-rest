from django.shortcuts import render, redirect

def index(request):
    print(request)
    user = request.user
    if user.is_authenticated:
        print(user)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
