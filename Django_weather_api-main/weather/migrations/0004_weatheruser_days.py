# Generated by Django 4.0.1 on 2022-07-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_alter_weatheruser_email_alter_weatheruser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatheruser',
            name='days',
            field=models.IntegerField(null=True),
        ),
    ]
