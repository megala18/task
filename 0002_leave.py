# Generated by Django 3.2.7 on 2021-10-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lfrom', models.IntegerField()),
                ('lto', models.IntegerField()),
                ('lreason', models.CharField(max_length=200)),
            ],
        ),
    ]