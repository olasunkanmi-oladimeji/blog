# Generated by Django 3.0.1 on 2020-01-09 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200109_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/blog'),
            preserve_default=False,
        ),
    ]
