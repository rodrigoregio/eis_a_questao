# Generated by Django 3.1.5 on 2021-01-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternativa',
            name='texto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
