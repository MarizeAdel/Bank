# Generated by Django 5.0.3 on 2024-03-28 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans',
            old_name='Interest_amount',
            new_name='_Interest_amount',
        ),
    ]
