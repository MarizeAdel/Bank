# Generated by Django 5.0.3 on 2024-03-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0006_alter_providerloan_interestrateforprovider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans',
            old_name='_Interest_amount',
            new_name='Interest_amount',
        ),
    ]
