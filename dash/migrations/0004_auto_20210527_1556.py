# Generated by Django 3.2.2 on 2021-05-27 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20210527_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]