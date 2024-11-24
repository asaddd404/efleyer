# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Fashion(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название слайдера")

    def __str__(self):
        return self.title


class SliderContent(models.Model):
    slider = models.ForeignKey(Fashion, related_name="contents", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.name} ({self.slider.title})"


class Electronic(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название слайдера")

    def __str__(self):
        return self.title


class SliderContent2(models.Model):
    slider = models.ForeignKey(Electronic, related_name="contents", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.name} ({self.slider.title})"


class Accessories(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название слайдера")

    def __str__(self):
        return self.title


class SliderContent3(models.Model):
    slider = models.ForeignKey(Accessories, related_name="contents", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return f"{self.name} ({self.slider.title})"


class Start(models.Model):
    name1 = models.CharField(max_length=100)
    nam2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name1


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.content_object.price
