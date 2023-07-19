# Generated by Django 4.2.2 on 2023-07-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0002_delete_exercicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('repeticoes', models.IntegerField()),
                ('series', models.IntegerField()),
                ('descanso', models.IntegerField()),
                ('musculo', models.CharField(max_length=100)),
            ],
        ),
    ]