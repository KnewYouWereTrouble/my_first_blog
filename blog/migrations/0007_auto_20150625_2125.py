# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(default=''),
        ),
    ]
