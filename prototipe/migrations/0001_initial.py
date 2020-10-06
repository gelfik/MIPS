# Generated by Django 3.1.1 on 2020-10-01 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predmet_name', models.CharField(default=None, max_length=256, unique=True, verbose_name='Название предмета')),
                ('predmet_name_sokr', models.CharField(default=None, max_length=20, unique=True, verbose_name='Название предмета сокращенно')),
                ('predmet_name_sokr_translite', models.CharField(blank=True, default=None, max_length=30, unique=True, verbose_name='Название предмета сокращенно англ')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'db_table': 'predmet',
            },
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(default=None, max_length=50, verbose_name='Название теста')),
                ('valid_date', models.DateField(default=None, verbose_name='Дата действия теста')),
                ('voprosi_count', models.PositiveSmallIntegerField(default=0, verbose_name='Число вопросов')),
                ('decision_time', models.TimeField(default=None, verbose_name='Время на решение теста')),
                ('active_status', models.BooleanField(blank=True, default=False, verbose_name='Статус публикации')),
                ('create_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель теста')),
                ('predmet_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='prototipe.predmet', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'db_table': 'test',
            },
        ),
        migrations.CreateModel(
            name='test_for_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Время создания теста')),
                ('end_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Время завершения теста')),
                ('ocenka', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Оценка')),
                ('end_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Решен/Не решен')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prototipe.test', verbose_name='Тест')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тест пользователя',
                'verbose_name_plural': 'Тесты пользователей',
                'db_table': 'test_for_user',
            },
        ),
        migrations.CreateModel(
            name='voprosi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vopros', models.TextField(default=None, verbose_name='Вопрос')),
                ('otvet', models.CharField(default=None, max_length=256, verbose_name='Ответ')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prototipe.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'voprosi',
            },
        ),
        migrations.CreateModel(
            name='test_for_user_voprosi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voprose_num', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Номер вопроса')),
                ('otvet_user', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Ответ пользователя')),
                ('otvet_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Правильно/Не правильно')),
                ('test_for_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prototipe.test_for_user', verbose_name='Тест пользователя')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('voprosi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prototipe.voprosi', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответы пользователей',
                'db_table': 'test_for_user_voprosi',
            },
        ),
    ]
