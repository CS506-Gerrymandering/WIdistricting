# Generated by Django 2.0.2 on 2018-04-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WIdistricting_App', '0016_auto_20180409_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pre_district',
            old_name='votes',
            new_name='total_votes',
        ),
        migrations.RemoveField(
            model_name='pre_district',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='pre_district',
            name='district_name',
        ),
        migrations.RemoveField(
            model_name='pre_district',
            name='party',
        ),
        migrations.AddField(
            model_name='pre_district',
            name='blue_votes',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='pre_district',
            name='red_votes',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
