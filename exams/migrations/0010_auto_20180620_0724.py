# Generated by Django 2.0.5 on 2018-06-20 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20180620_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_body_image_1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_body_image_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_body_image_3',
        ),
    ]
