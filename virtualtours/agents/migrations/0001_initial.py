# Generated by Django 2.1.1 on 2018-09-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('doj', models.DateTimeField(verbose_name='Date Joined')),
                ('contact', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
