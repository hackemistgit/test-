# Generated by Django 3.1.4 on 2020-12-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0002_auto_20191219_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorlist',
            name='names',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
