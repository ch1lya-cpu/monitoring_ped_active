# Generated by Django 3.0.7 on 2020-06-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0019_auto_20200618_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers_has_event',
            options={'verbose_name': 'Преподаватель + события', 'verbose_name_plural': 'Преподаватели + события'},
        ),
        migrations.AlterModelOptions(
            name='teachers_has_qualific_course',
            options={'verbose_name': 'Преподаватели + квалификационный курс', 'verbose_name_plural': 'Преподаватели + квалификационные курсы'},
        ),
        migrations.AlterModelOptions(
            name='teachers_in_pck',
            options={'verbose_name': 'Преподаватели + ПЦК', 'verbose_name_plural': 'Преподаватели + ПЦК'},
        ),
    ]