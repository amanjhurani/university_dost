# Generated by Django 2.0.5 on 2018-05-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0004_university_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ('-pk',), 'verbose_name_plural': 'universities'},
        ),
    ]
