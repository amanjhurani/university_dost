# Generated by Django 2.0.5 on 2018-12-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0011_auto_20180620_0726'),
        ('users', '0003_auto_20180828_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='voted_questions',
            field=models.ManyToManyField(related_name='voted_questions', to='exams.Question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='questions',
            field=models.ManyToManyField(related_name='questions', to='exams.Question'),
        ),
    ]
