# Generated by Django 4.0.8 on 2023-05-16 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_rename_seo_data_seo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_media_s',
            name='company',
        ),
        migrations.RemoveField(
            model_name='website_s',
            name='company',
        ),
        migrations.DeleteModel(
            name='Seo_s',
        ),
        migrations.DeleteModel(
            name='Social_media_s',
        ),
        migrations.DeleteModel(
            name='Website_s',
        ),
    ]
