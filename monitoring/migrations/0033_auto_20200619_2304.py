# Generated by Django 3.0.7 on 2020-06-19 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0032_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Активность', 'verbose_name_plural': 'Активности'},
        ),
    ]
