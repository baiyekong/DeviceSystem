# Generated by Django 2.2.2 on 2019-06-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.CharField(max_length=128, unique=True, verbose_name='时间'),
        ),
    ]
