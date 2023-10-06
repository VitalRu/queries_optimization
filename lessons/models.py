from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField(verbose_name='длительность сек.')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название продукта')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='владелец',
        blank=True,
    )
    lesson = models.ManyToManyField(
        Lesson,
        through='ProductLesson',
        related_name='lesson_products',
        verbose_name='уроки продукта'
    )

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='accessed_products',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user} has access to {self.product}'


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
