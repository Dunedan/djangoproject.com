# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 09:19
from __future__ import unicode_literals

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_document_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(editable=False, null=True),
        ),
        migrations.AddIndex(
            model_name='document',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search'], name='docs_docume_search_5dc895_gin'),
        ),
    ]
