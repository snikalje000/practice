# Generated by Django 4.1.3 on 2023-08-26 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatdata',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 17, 49, 948515, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 17, 54, 334384, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enrolldata',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 17, 58, 117379, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featuredevent',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 18, 1, 731177, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phonedata',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 18, 4, 416374, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscribe_data',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 18, 7, 245736, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcoming_popup',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 18, 10, 446511, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcomingevent',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 8, 26, 6, 18, 13, 740590, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
