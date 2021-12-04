# Generated by Django 3.2.3 on 2021-10-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_auto_20211021_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='cms_app.Tag'),
        ),
    ]
