# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('tele', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('addr', models.CharField(max_length=100)),
                ('birth', models.DateField()),
            ],
        ),
    ]
