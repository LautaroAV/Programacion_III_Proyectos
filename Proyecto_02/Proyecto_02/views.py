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

def MakeUpApiAll(request):
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?"
    response = urlopen(url)
    data = json.loads(response.read())
    context = { 'data': data}
    return render(request, 'index.html', context)

def MakeUpApi(request,type_p):
    if type_p:
        url = "http://makeup-api.herokuapp.com/api/v1/products.json?product_type="
        url += type_p
    response = urlopen(url)
    data = json.loads(response.read())
    context = { 'data': data}
    return render(request, 'index.html', context)

def MakeupApiTag(request,type_p,tag):
    devolver_tag_list = []
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?product_type="
    url += type_p
    response = urlopen(url)
    data = json.loads(response.read())
    for i in data:
        for k in i["tag_list"]:
            if k == tag:
                devolver_tag = i
                devolver_tag_list.append(devolver_tag)
                context = { 'data': devolver_tag_list}
    return render(request, 'index.html', context)