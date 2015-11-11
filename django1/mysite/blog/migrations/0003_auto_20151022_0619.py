# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_core_praise_servant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('audio', models.FileField(upload_to='sermons')),
            ],
        ),
        migrations.AlterField(
            model_name='core',
            name='picture',
            field=models.ImageField(upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='praise',
            name='picture',
            field=models.ImageField(upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='servant',
            name='picture',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]
