from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def contact(request):
    print("You are at function Contact")
    return render(request, 'contact.html')
