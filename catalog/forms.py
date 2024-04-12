from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    __blocked_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'price', 'image')

    def clean_name(self):
        cleaned_data = super().cleaned_data['name']
        for name in self.__blocked_name:
            if name in cleaned_data:
                raise forms.ValidationError('Запрещенное имя продукта')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ('name', 'number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'