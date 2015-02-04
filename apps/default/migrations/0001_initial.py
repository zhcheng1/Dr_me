# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('address', models.TextField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('sex', models.CharField(default=b'FEMALE', max_length=2, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female'), (b'OTHER', b'Other')])),
                ('specialty', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('appointment', models.ForeignKey(to='default.Appointment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
