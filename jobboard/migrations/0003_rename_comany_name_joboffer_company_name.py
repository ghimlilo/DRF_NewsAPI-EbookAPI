# Generated by Django 4.0 on 2022-02-07 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0002_alter_joboffer_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joboffer',
            old_name='comany_name',
            new_name='company_name',
        ),
    ]
