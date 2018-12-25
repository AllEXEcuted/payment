# Generated by Django 2.1.1 on 2018-12-21 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=16, null=True, verbose_name='Номер карты')),
                ('card_info', models.CharField(max_length=5, null=True, verbose_name='Месяц, год действия карты')),
                ('cvc', models.CharField(max_length=3, null=True, verbose_name='CVC')),
                ('how_many', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(75000)], verbose_name='Сколько')),
                ('comment', models.TextField(max_length=150, null=True, verbose_name='Комментарий')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Эл.почта')),
            ],
        ),
        migrations.CreateModel(
            name='FromYourBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=12, null=True, verbose_name='ИНН')),
                ('bik', models.CharField(max_length=9, null=True, verbose_name='БИК')),
                ('account_number', models.CharField(max_length=20, null=True, verbose_name='Номер счёта')),
                ('nds', models.CharField(choices=[('НДС 18%', 'НДС 18%'), ('НДС 10%', 'НДС 10%'), ('без НДС', 'без НДС')], max_length=10, null=True, verbose_name='За что')),
                ('how_many', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(75000)], verbose_name='Сколько')),
            ],
        ),
        migrations.CreateModel(
            name='RequestedPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=12, null=True, verbose_name='ИНН')),
                ('bik', models.CharField(max_length=9, null=True, verbose_name='БИК')),
                ('account_number', models.CharField(max_length=20, null=True, verbose_name='Номер счёта')),
                ('how_many', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(75000)], verbose_name='Сколько')),
                ('phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Эл.почта')),
                ('nds', models.CharField(choices=[('НДС 18%', 'НДС 18%'), ('НДС 10%', 'НДС 10%'), ('без НДС', 'без НДС')], max_length=10, null=True, verbose_name='За что')),
            ],
        ),
    ]