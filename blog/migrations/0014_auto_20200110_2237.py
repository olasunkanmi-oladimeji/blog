# Generated by Django 3.0.1 on 2020-01-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200110_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
