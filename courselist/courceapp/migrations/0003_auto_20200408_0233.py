# Generated by Django 2.1.5 on 2020-04-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courceapp', '0002_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]
