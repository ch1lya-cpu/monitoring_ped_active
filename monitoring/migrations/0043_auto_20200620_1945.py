# Generated by Django 3.0.7 on 2020-06-20 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0042_remove_teacher_pck_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='pck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.PCK'),
        ),
        migrations.DeleteModel(
            name='Teachers_in_PCK',
        ),
    ]