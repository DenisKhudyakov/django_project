from django.shortcuts import render


def contacts(request):
    return render(request,'catalog/contacts/contacts.html' )


def home(request):
    return render(request,'catalog/contacts/home.html')
