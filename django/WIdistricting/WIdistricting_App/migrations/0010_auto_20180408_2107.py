# Generated by Django 2.0.2 on 2018-04-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WIdistricting_App', '0009_auto_20180408_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_district',
            name='district_name',
            field=models.CharField(default='None', max_length=100, primary_key=True, serialize=False),
        ),
    ]
