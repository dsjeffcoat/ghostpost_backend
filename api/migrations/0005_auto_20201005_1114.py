# Generated by Django 3.1.2 on 2020-10-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201002_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='is_boast',
            field=models.CharField(blank=True, choices=[('Boast', 'Boast'), ('Roast', 'Roast')], max_length=5, null=True),
        ),
    ]
