# Generated by Django 3.0.7 on 2020-06-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_teacher_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория мероприятия', 'verbose_name_plural': 'Категории мероприятий'},
        ),
        migrations.AlterModelOptions(
            name='criterie',
            options={'verbose_name': 'Система оценивания', 'verbose_name_plural': 'Система оценивания'},
        ),
        migrations.AlterModelOptions(
            name='type_educ',
            options={'verbose_name': 'Тип образования', 'verbose_name_plural': 'Типы образования'},
        ),
        migrations.RemoveField(
            model_name='staging_on_teacher',
            name='teacher_name',
        ),
        migrations.AlterField(
            model_name='achievement',
            name='criterie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Criterie', verbose_name='Система оценивания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=45, verbose_name='Название категории мероприятия'),
        ),
        migrations.AlterField(
            model_name='criterie',
            name='categoryes_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Category', verbose_name='Категория мероприятия'),
        ),
        migrations.AlterField(
            model_name='qualific_course',
            name='date_end',
            field=models.DateField(verbose_name='Дата конца курса повышения квалификации'),
        ),
        migrations.AlterField(
            model_name='qualific_course',
            name='date_start',
            field=models.DateField(verbose_name='Дата начала курса повышения квалификации'),
        ),
        migrations.AlterField(
            model_name='qualific_course',
            name='place',
            field=models.CharField(max_length=100, verbose_name='Место курса повышения квалификации'),
        ),
        migrations.AlterField(
            model_name='qualific_course',
            name='topic',
            field=models.CharField(max_length=200, verbose_name='Тема курса повышения квалификации'),
        ),
        migrations.AlterField(
            model_name='staging_on_teacher',
            name='teacher_role',
            field=models.CharField(max_length=60, verbose_name='Роль преподавателя в мероприятии'),
        ),
        migrations.AlterField(
            model_name='type_educ',
            name='educ_name',
            field=models.CharField(max_length=50, verbose_name='Тип образования'),
        ),
        migrations.DeleteModel(
            name='Teachers_has_type_educ',
        ),
    ]
