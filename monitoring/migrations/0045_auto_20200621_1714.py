# Generated by Django 3.0.7 on 2020-06-21 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0044_auto_20200621_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Активность', 'verbose_name_plural': 'Активности'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='events',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Event', verbose_name='Событие'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='teachers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Teacher', verbose_name='Преподаватель'),
        ),
    ]
