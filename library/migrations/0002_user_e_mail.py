# Generated by Django 4.0.5 on 2022-06-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='e_mail',
            field=models.EmailField(max_length=354, null=True),
        ),
    ]
