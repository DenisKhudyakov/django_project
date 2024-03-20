from django.db import models

NULL_PARAM = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(max_length=150, verbose_name='описание товара')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULL_PARAM)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена в руб')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULL_PARAM)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



