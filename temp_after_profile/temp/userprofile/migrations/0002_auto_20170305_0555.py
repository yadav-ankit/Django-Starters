# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Skills',
            new_name='skills',
        ),
    ]
