# Generated by Django 3.0.7 on 2020-06-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0034_auto_20200619_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='event',
            new_name='events',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='teacher',
            new_name='teachers',
        ),
        migrations.AddField(
            model_name='activity',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
