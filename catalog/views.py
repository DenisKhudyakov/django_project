from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def basket(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/basket.html', context=context)


def card(request, pk):
    product = {
        'products': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product_card.html', context=product)
