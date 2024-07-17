# Generated by Django 5.0.7 on 2024-07-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='bonuses',
        ),
        migrations.AddField(
            model_name='productsize',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='set',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.topping', verbose_name='Добавки'),
        ),
    ]
