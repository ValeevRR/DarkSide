# Generated by Django 3.2 on 2021-04-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sithWay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitanswer',
            name='answer',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ответ'),
        ),
    ]