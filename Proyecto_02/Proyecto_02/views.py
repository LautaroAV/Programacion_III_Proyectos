from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from urllib.request import urlopen
import json


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = { 'form': form}
    return render(request, 'register.html', context)

def DigimonApi(request):
    url = "https://digimon-api.vercel.app/api/digimon"

    response = urlopen(url)
    data = json.loads(response.read())
    context = { 'data': data}
    return render(request, 'index.html', context)