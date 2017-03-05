# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20170305_0555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='users',
            new_name='user',
        ),
    ]
