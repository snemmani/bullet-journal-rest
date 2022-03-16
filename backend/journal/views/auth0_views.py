from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout

from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

def index(request):
    print(request)
    user = request.user
    if user.is_authenticated:
        print(user)
        return render(request, 'index.html')
    else:
        return redirect(reverse('social:begin', args=["auth0"]))


def logout_user(request):
    logout(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/bujo/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
