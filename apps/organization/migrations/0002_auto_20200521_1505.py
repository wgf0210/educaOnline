# Generated by Django 2.2.5 on 2020-05-21 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200521_1505'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='city',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='org',
        ),
        migrations.DeleteModel(
            name='CityDict',
        ),
        migrations.DeleteModel(
            name='CourseOrg',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
