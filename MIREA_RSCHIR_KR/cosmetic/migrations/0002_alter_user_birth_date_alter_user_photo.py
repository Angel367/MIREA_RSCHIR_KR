# Generated by Django 5.0 on 2023-12-07 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]