# Generated by Django 2.2 on 2020-02-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200210_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]
