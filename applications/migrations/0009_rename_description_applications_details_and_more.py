# Generated by Django 5.2.3 on 2025-07-12 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_rename_package_id_applications_app_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='description',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='app_quality_score',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='avg_rating',
            new_name='sentiment_score',
        ),
    ]
