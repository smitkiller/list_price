# Generated by Django 4.1 on 2022-08-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_image', models.ImageField(upload_to='images/')),
                ('action', models.CharField(choices=[('', '--- Select Action ---'), ('ADD_DATA', 'add data'), ('SEARCH', 'search')], max_length=50)),
                ('file_name', models.CharField(max_length=120, verbose_name='File Name')),
                ('features', models.CharField(max_length=500, verbose_name='Features')),
            ],
        ),
    ]
