# Generated by Django 3.0.7 on 2020-06-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_auto_20200617_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='rang',
            field=models.CharField(max_length=45, null=True, verbose_name='Разряд/соответсвие ПС'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(max_length=60, null=True, verbose_name='Квалификация'),
        ),
    ]
