# Generated by Django 3.0.7 on 2020-06-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0040_auto_20200620_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='pck_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.PCK'),
        ),
    ]