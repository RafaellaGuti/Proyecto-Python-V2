# Generated by Django 4.2.4 on 2023-08-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
