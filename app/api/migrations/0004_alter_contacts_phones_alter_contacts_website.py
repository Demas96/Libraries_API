# Generated by Django 4.2.5 on 2023-09-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_locale_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phones',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='website',
            field=models.TextField(blank=True, default=None),
        ),
    ]