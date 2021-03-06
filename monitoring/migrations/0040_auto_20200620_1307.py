# Generated by Django 3.0.7 on 2020-06-20 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0039_auto_20200620_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='pck_id',
        ),
        migrations.CreateModel(
            name='Teachers_in_PCK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.PCK')),
                ('teachers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Qualific_course_for_Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qual_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Qualification_course')),
                ('teachers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Teacher')),
            ],
        ),
    ]
