# Generated by Django 4.0.8 on 2023-02-07 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_performance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='paid_est_cpc_budget',
            new_name='paid_est_ppc_budget',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='web_social_sources',
        ),
    ]
