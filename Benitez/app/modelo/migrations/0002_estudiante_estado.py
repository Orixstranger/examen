# Generated by Django 2.1.3 on 2018-11-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
