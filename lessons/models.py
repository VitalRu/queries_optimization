from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField(verbose_name='длительность в секундах')


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название продукта')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='владелец',
    )
    lesson = models.ManyToManyField(
        Lesson,
        through='ProductLesson',
        related_name='product_lessons',
        verbose_name='уроки продукта'
    )


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='accessed_products',
        on_delete=models.CASCADE,
    )


class ProductLesson(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='products',
    )
