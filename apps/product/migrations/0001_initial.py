# Generated by Django 5.0.7 on 2024-07-17 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Описание')),
                ('description_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('description_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_photos/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='topping_photos/', verbose_name='Фото')),
                ('possibly_remove', models.BooleanField(default=False, verbose_name='Возможность удаления')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Описание')),
                ('description_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('description_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='topping_photos/', verbose_name='Фото')),
                ('bonuses', models.BooleanField(default=False, verbose_name='Можно оптатить бонусами')),
            ],
            options={
                'verbose_name': 'Добавка',
                'verbose_name_plural': 'Добавки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='topping_photos/', verbose_name='Фото')),
                ('bonuses', models.BooleanField(default=False, verbose_name='Можно оптатить бонусами')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='Категория')),
                ('ingredients', models.ManyToManyField(related_name='products', to='product.ingredient', verbose_name='Ингредиенты')),
                ('toppings', models.ManyToManyField(related_name='products', to='product.topping', verbose_name='Добавки')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='product.product', verbose_name='Продукт')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='product.size', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Цена продукта по размеру',
                'verbose_name_plural': 'Цены продуктов по размерам',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='topping_photos/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('bonuses', models.BooleanField(default=False, verbose_name='Можно оптатить бонусами')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='product.category', verbose_name='Категория')),
                ('products', models.ManyToManyField(related_name='sets', to='product.productsize', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Сет',
                'verbose_name_plural': 'Сеты',
            },
        ),
    ]
