# Generated by Django 4.0.5 on 2022-08-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_sector_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_active',
            field=models.BigIntegerField(),
        ),
    ]