# Generated by Django 2.2.10 on 2020-02-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('phone', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('address', models.CharField(max_length=128, unique=True, verbose_name='адресс')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='краткое описание продукта')),
                ('description', models.TextField(blank=True, verbose_name='описание продукта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
    ]
