# Generated by Django 2.0 on 2021-02-06 17:32

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('me', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', base.models.BigBigField()),
                ('g', base.models.BigBigField()),
                ('y', base.models.BigBigField()),
                ('x', base.models.BigBigField(blank=True, null=True)),
            ],
        ),
    ]
