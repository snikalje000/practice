# Generated by Django 4.1.3 on 2023-08-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0010_contactus_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonedata',
            name='cell1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='cell2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='date',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='lead_assigned',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='lead_in_source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='lead_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonedata',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
