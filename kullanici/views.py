
from django.shortcuts import render
from django.http import HttpResponse

def ana_sayfa(request):
    return HttpResponse("<h1>Django Dünyasına Hoş Geldin!</h1><p>İlk sayfamız başarıyla çalışıyor.</p>")
# Create your views here.
