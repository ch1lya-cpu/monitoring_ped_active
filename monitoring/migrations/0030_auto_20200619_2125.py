# Generated by Django 3.0.7 on 2020-06-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0029_auto_20200619_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='ball',
            field=models.FloatField(null=True, verbose_name='Балл'),
        ),
    ]
