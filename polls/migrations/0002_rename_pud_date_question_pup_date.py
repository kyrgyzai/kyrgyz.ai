# Generated by Django 3.2.8 on 2021-10-10 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pud_date',
            new_name='pup_date',
        ),
    ]