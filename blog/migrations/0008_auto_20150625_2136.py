# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150625_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='snippet',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
