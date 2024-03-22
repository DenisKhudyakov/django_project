from django.shortcuts import render


def contacts(request):
    return render(request,'catalog/contacts.html')


def basket(request):
    return render(request, 'catalog/basket.html')

