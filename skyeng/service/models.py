from django.db import models
import datetime
from datetime import datetime, timedelta
from django.db.models import Count


class Product(models.Model):
    ACTIVITY_STATUS_CHOICE = [
        (True, 'активность есть'),
        (False, 'активности нет'),
    ]
    product_id = models.IntegerField(
        verbose_name='айди',
        unique=True
    )
    name = models.CharField(
        verbose_name='название',
        max_length=300
    )
    category = models.CharField(
        verbose_name='категория',
        max_length=100
    )
    activity_status = models.BooleanField(
        verbose_name='статус активности',
        choices=ACTIVITY_STATUS_CHOICE,
        default=True
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'информация о товаре'
        verbose_name_plural = 'информация о товарах'
        ordering = ['category']

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(
        verbose_name='заказ',
        to='service.Product',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    orders_last_month = models.IntegerField(
        verbose_name='заказы за прошлый месяц'
    )
    order_with_first_day = models.IntegerField(
        verbose_name='заказы с 1 дня месяца'
    )

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['product']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        today = datetime.today()
        first_day_of_month = datetime(today.year, today.month, 1)
        products_last_month = self.product.__class__.objects.filter(
            orders__created_at__gte=first_day_of_month - timedelta(days=30),
            orders__created_at__lte=first_day_of_month - timedelta(days=1)
        ).annotate(count=Count('product_id')).values_list('count', flat=True)
        self.orders_last_month = sum(products_last_month)
        self.order_with_first_day = self.product.__class__.objects.filter(
            orders__created_at__gte=first_day_of_month
        ).count()
