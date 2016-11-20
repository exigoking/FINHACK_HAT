# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FINHack_mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
    ]
