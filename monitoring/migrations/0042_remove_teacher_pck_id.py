# Generated by Django 3.0.7 on 2020-06-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0041_teacher_pck_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='pck_id',
        ),
    ]
