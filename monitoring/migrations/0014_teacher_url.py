# Generated by Django 3.0.7 on 2020-06-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0013_auto_20200617_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='url',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
    ]
