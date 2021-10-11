# Generated by Django 3.2.7 on 2021-10-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio_a_to_b', models.FloatField()),
            ],
            options={
                'db_table': 'answers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AverageCharactersRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'average_characters_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('height', models.IntegerField()),
                ('short_description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'characters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField()),
                ('analysis_usage', models.BooleanField()),
                ('concordance_factor', models.FloatField()),
            ],
            options={
                'db_table': 'polls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]