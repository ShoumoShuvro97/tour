# Generated by Django 4.1 on 2022-09-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourist',
            name='is_visit',
            field=models.BooleanField(default=False),
        ),
    ]
