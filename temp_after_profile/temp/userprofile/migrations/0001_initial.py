# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('college', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('Skills', models.CharField(max_length=50)),
                ('users', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
