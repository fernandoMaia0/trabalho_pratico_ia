# Generated by Django 5.1.2 on 2024-12-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='nome',
            field=models.CharField(default='Desconhecido', max_length=100),
        ),
    ]