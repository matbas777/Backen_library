# Generated by Django 4.0.5 on 2022-06-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_user_e_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='date_of_delivery',
            field=models.DateField(null=True),
        ),
    ]