# Generated by Django 2.0.5 on 2018-05-23 16:04

import config.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0002_auto_20180523_1542'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=128)),
                ('year', models.CharField(max_length=4)),
                ('term', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter')], max_length=12)),
                ('date', models.DateField()),
                ('total_time', models.CharField(max_length=12)),
                ('total_marks', models.IntegerField()),
                ('unique_code', models.CharField(blank=True, max_length=12, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.CharField(max_length=128)),
                ('question_body', models.CharField(max_length=1000)),
                ('question_body_image_1', models.ImageField(blank=True, null=True, upload_to=config.utils.upload_question_body_path)),
                ('question_body_image_2', models.ImageField(blank=True, null=True, upload_to=config.utils.upload_question_body_path)),
                ('question_body_image_3', models.ImageField(blank=True, null=True, upload_to=config.utils.upload_question_body_path)),
                ('question_type', models.CharField(choices=[('mcq', 'MCQ'), ('short_question', 'Short Question'), ('descriptive_question', 'Descriptive Question')], max_length=12)),
                ('answer', models.TextField()),
                ('explanation', models.TextField()),
                ('marks', models.IntegerField()),
                ('vote', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
            ],
        ),
    ]
