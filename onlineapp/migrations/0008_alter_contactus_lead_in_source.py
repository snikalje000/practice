# Generated by Django 4.1.3 on 2023-08-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0007_alter_contactus_lead_in_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='lead_in_source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]