# Generated by Django 3.2.3 on 2021-10-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
