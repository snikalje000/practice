# Generated by Django 4.1.3 on 2023-08-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0008_alter_contactus_lead_in_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='cell1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='cell2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
