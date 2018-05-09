# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='id_ubigeo',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='vc_usuarioCrea',
            field=models.CharField(default=b'cvargas', max_length=50),
        ),
    ]
