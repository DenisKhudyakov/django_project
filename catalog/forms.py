from django import forms

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):

    __blocked_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'description', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for name in self.__blocked_name:
            if name in cleaned_data:
                raise forms.ValidationError('Запрещенное имя продукта')
        return cleaned_data


class ProductModeratorForm(StyleMixin, forms.ModelForm):

    __blocked_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for name in self.__blocked_name:
            if name in cleaned_data:
                raise forms.ValidationError('Запрещенное имя продукта')
        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

