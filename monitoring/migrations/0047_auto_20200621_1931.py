# Generated by Django 3.0.7 on 2020-06-21 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0046_activity_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Tag', verbose_name='Категория и подкатегория'),
        ),
    ]
