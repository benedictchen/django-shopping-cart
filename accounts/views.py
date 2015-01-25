from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
