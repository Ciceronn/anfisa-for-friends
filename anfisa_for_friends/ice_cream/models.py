from django.db import models
from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)
    slug = models.SlugField(verbose_name='Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=100)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)
    slug = models.SlugField(verbose_name='Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)

    class Meta:
        verbose_name = 'обертка'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    is_on_main = models.BooleanField(verbose_name='На главную', default=False)
    title = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинги')

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
