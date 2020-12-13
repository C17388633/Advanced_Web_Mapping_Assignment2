# Generated by Django 3.1.1 on 2020-12-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_airport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='a_lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='a_lon',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='a_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='airport',
            name='a_id',
        ),
        migrations.AlterField(
            model_name='airport',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
