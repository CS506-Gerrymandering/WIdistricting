# Generated by Django 2.0.2 on 2018-04-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WIdistricting_App', '0014_pre_district_district_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_district',
            name='pre_district_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pre_district',
            name='district_name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
