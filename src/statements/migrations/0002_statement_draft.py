# Generated by Django 3.2.4 on 2021-07-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='draft',
            field=models.TextField(default='false'),
        ),
    ]