# Generated by Django 4.1.4 on 2023-01-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_about_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='subtitle',
            field=models.CharField(max_length=900),
        ),
    ]
