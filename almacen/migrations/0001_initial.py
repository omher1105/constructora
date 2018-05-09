# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_proyecto', models.IntegerField()),
                ('vc_codTipoDocumento', models.CharField(max_length=3)),
                ('vc_numDocumento', models.CharField(max_length=12)),
                ('vc_nombreProyecto', models.CharField(max_length=120)),
                ('vc_direccion', models.CharField(max_length=200)),
                ('dt_fecAprobacion', models.DateTimeField(auto_now_add=True)),
                ('dt_fecInicio', models.DateTimeField(auto_now_add=True)),
                ('dt_fecCierre', models.DateTimeField(auto_now_add=True)),
                ('id_colaborador', models.IntegerField()),
                ('vc_nomContacto', models.CharField(max_length=120)),
                ('vc_telfContacto', models.CharField(max_length=120)),
                ('b_flagInactivo', models.BooleanField()),
                ('dt_crea', models.DateTimeField(auto_now_add=True)),
                ('vc_ipCrea', models.CharField(max_length=20)),
                ('dt_edita', models.DateTimeField(auto_now_add=True)),
                ('vc_usuarioEdita', models.CharField(max_length=50)),
                ('vc_ipEdita', models.CharField(max_length=20)),
            ],
        ),
    ]
