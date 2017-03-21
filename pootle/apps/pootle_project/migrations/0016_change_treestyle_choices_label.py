# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_project', '0015_rename_fs_treestyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='treestyle',
            field=models.CharField(choices=[('auto', 'Automatic detection of GNU/non-GNU file layouts (slower)'), ('gnu', 'GNU style: files named by language code'), ('nongnu', 'Non-GNU: Each language in its own directory'), ('pootle_fs', 'Allow Pootle FS to manage filesystems (Experimental)')], default='auto', max_length=20, verbose_name='Project Tree Style'),
        ),
    ]
