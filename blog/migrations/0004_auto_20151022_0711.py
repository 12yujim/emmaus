# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151022_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='core',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='praise',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='servant',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
