import json

import requests
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def index(request):
    return render(request, 'index.html')


def display_gif(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        keyword = form.data['keyword']
        data = requests.get('https://api.giphy.com/v1/gifs/search?q=[' + keyword + ']&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1', params=request.GET)
        result = json.loads(data.text)
        giphy_link = result['data'][0]['images']['original']['url']
        return redirect(giphy_link)
