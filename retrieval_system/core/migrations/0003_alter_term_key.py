# Generated by Django 4.0.8 on 2022-12-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_inser_cranfield_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
