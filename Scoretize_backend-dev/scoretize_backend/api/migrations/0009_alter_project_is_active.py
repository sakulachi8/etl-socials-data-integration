# Generated by Django 4.0.5 on 2022-08-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_project_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_active',
            field=models.BigIntegerField(default=True),
        ),
    ]
