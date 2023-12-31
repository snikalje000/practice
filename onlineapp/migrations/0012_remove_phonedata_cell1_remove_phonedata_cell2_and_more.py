# Generated by Django 4.1.3 on 2023-08-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0011_phonedata_cell1_phonedata_cell2_phonedata_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonedata',
            name='cell1',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='cell2',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='lead_assigned',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='lead_in_source',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='lead_status',
        ),
        migrations.RemoveField(
            model_name='phonedata',
            name='notes',
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='cell1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='cell2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='date',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='lead_assigned',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='lead_in_source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='lead_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
