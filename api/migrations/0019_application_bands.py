# Generated by Django 3.1 on 2021-05-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20210319_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='bands',
            field=models.CharField(default='B2, B3, B4', max_length=200),
        ),
    ]
