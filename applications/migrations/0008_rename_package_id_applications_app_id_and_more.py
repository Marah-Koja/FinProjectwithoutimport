# Generated by Django 5.2.3 on 2025-07-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_rename_rating_applications_app_quality_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='package_id',
            new_name='app_id',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='negative_percent',
            new_name='negative',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='neutral_percent',
            new_name='neutral',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='positive_percent',
            new_name='positive',
        ),
        migrations.AddField(
            model_name='applications',
            name='total_comments',
            field=models.IntegerField(default=0.0),
        ),
    ]
