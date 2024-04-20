from django.db import models

from config import settings

NULL_PARAM = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание товара')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULL_PARAM)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена в руб')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULL_PARAM)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, **NULL_PARAM, verbose_name='продавец')

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):

    """Модель версия продукта"""
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions')
    number = models.PositiveIntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=100, verbose_name='название версии')
    current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name} - {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'



