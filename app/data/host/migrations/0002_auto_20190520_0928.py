# Generated by Django 2.2 on 2019-05-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='host',
            field=models.URLField(),
        ),
    ]
