# Generated by Django 4.0.1 on 2022-07-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_weatheruser_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatheruser',
            name='days',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
