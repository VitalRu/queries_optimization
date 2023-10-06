from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField(verbose_name='длительность сек.')

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='view_lesson'
    )
    view_time = models.DateTimeField(auto_now_add=True)
    view_duration = models.IntegerField(
        verbose_name='длительность просмотра сек.'
    )


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название продукта')
    lesson = models.ManyToManyField(
        Lesson,
        through='ProductLesson',
        related_name='lesson_products',
        verbose_name='уроки продукта'
    )

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_accessed',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='accessed_products',
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

    class Meta:
        verbose_name = 'Урок в продукте'
        verbose_name_plural = 'Уроки в продукте'
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'lesson'),
                name='unique_product_lesson'
            ),
        )
