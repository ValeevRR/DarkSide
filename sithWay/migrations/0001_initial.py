# Generated by Django 3.2 on 2021-04-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTest',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Орден испытания',
                'verbose_name_plural': 'Ордены испытания',
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': ' Планеты',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя рекрута')),
                ('age', models.SmallIntegerField(verbose_name='Возраст рекрута')),
                ('email', models.EmailField(max_length=254, verbose_name='EMail рекрута')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sithWay.planet', verbose_name='Планета обитания')),
            ],
            options={
                'verbose_name': 'Рекрут',
                'verbose_name_plural': 'Рекруты',
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос испытания')),
                ('answer', models.BooleanField(verbose_name='Правильный ответ')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sithWay.ordertest')),
            ],
            options={
                'verbose_name': 'Вопрос испытания',
                'verbose_name_plural': 'Воспросы испытания',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя ситха')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sithWay.planet', verbose_name='Планета обучения')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
            },
        ),
        migrations.CreateModel(
            name='RecruitAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sithWay.testquestion', verbose_name='Вопрос')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sithWay.recruit', verbose_name='Рекрут')),
            ],
            options={
                'verbose_name': 'Ответ рекрута',
                'verbose_name_plural': 'Ответы рекрутов',
            },
        ),
        migrations.AddField(
            model_name='recruit',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sithWay.sith', verbose_name='Планета обитания'),
        ),
    ]
