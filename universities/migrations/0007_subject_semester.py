# Generated by Django 2.0.5 on 2018-12-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_auto_20180610_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.IntegerField(default=2),
        ),
    ]
