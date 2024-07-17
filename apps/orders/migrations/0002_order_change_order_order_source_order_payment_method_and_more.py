# Generated by Django 5.0.7 on 2024-07-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='change',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сдача'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_source',
            field=models.CharField(choices=[('mobile', 'Мобильное приложение'), ('web', 'Веб-сайт'), ('unknown', 'Неизвестно')], default='unknown', max_length=10, verbose_name='Источник заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Карта'), ('cash', 'Наличные'), ('online', 'Онлайн')], default='card', max_length=255, verbose_name='Способ оплаты'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_bonus',
            field=models.BooleanField(default=False, verbose_name='Бонусный продукт'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opening_hours',
            field=models.TimeField(blank=True, null=True, verbose_name='Часы работы'),
        ),
    ]
