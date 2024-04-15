from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = Product

    def get_context_data(self,*args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(current_version=True)
            if active_versions:
                product.name_version = active_versions.last().name
                product.number_version = active_versions.last().number
        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


class VersionListView(ListView):
    model = Version

    # def get_queryset(self, *args, **kwargs):
        # queryset = Version.objects.all()
        # products = Product.objects.all()
        # for product in products:
        #     print(product)
        #     versions = Version.objects.filter(product=product)
        #     print(queryset.product == product)
        #     return versions


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')


class VersionDetailView(DetailView):
    model = Version
    context_object_name = 'versions'


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:versions')






