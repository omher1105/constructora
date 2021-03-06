# Generated by Django 2.0.5 on 2018-05-10 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('vc_codEstado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('vc_numDocumento', models.CharField(db_column='vc_numDocumento', max_length=12)),
                ('vc_razonSocial', models.CharField(db_column='vc_razonSocial', max_length=120)),
                ('vc_correo', models.CharField(blank=True, max_length=80, null=True)),
                ('vc_direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('vc_contacto', models.CharField(blank=True, max_length=120, null=True)),
                ('vc_telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('b_flaginactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id_colaborador', models.AutoField(primary_key=True, serialize=False)),
                ('vc_codigocolaborador', models.CharField(blank=True, db_column='vc_codigoColaborador', max_length=3, null=True)),
                ('vc_codcondicion', models.CharField(blank=True, db_column='vc_codCondicion', max_length=3, null=True)),
                ('vc_codtipotrabajador', models.CharField(blank=True, db_column='vc_codTipoTrabajador', max_length=3, null=True)),
                ('bl_fldiscapasitado', models.TextField(blank=True, db_column='bl_flDiscapasitado', null=True)),
                ('vc_codtipodocumento', models.CharField(db_column='vc_codTipoDocumento', max_length=3)),
                ('vc_numdocumento', models.CharField(db_column='vc_numDocumento', max_length=12)),
                ('vc_nomColaborador', models.CharField(db_column='vc_nomColaborador', max_length=50)),
                ('vc_apePatColaborador', models.CharField(db_column='vc_apePatColaborador', max_length=50)),
                ('vc_apematcolaborador', models.CharField(db_column='vc_apeMatColaborador', max_length=50)),
                ('vc_direccioncolaborador', models.CharField(blank=True, db_column='vc_direccionColaborador', max_length=150, null=True)),
                ('vc_correopersonal', models.CharField(blank=True, db_column='vc_correoPersonal', max_length=100, null=True)),
                ('vc_correocorporativo', models.CharField(blank=True, db_column='vc_correoCorporativo', max_length=100, null=True)),
                ('dt_fecnacimiento', models.DateField(blank=True, db_column='dt_fecNacimiento', null=True)),
                ('dt_fecingreso', models.DateField(blank=True, db_column='dt_fecIngreso', null=True)),
                ('dt_feccese', models.DateField(blank=True, db_column='dt_fecCese', null=True)),
                ('vc_telfcolaborador', models.CharField(blank=True, db_column='vc_telfColaborador', max_length=10, null=True)),
                ('vc_codestado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('b_flaginactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Colaborador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColaboradoresCargo',
            fields=[
                ('id_colaboradoresCargo', models.AutoField(db_column='id_colaboradoresCargo', primary_key=True, serialize=False)),
                ('b_flagInactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Colaboradores_Cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id_general', models.AutoField(primary_key=True, serialize=False)),
                ('vc_nomtabla', models.CharField(db_column='vc_nomTabla', max_length=45)),
                ('vc_descripcion', models.CharField(max_length=150)),
                ('vc_codestado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('b_flaginactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'General',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralDetalle',
            fields=[
                ('id_generalDetalle', models.AutoField(db_column='id_generalDetalle', primary_key=True, serialize=False)),
                ('vc_codigo', models.CharField(max_length=3)),
                ('vc_valor1', models.CharField(max_length=45)),
                ('vc_valor2', models.CharField(blank=True, max_length=45, null=True)),
                ('vc_valor3', models.CharField(blank=True, max_length=45, null=True)),
                ('vc_valor4', models.CharField(blank=True, max_length=45, null=True)),
                ('txt_valor5', models.TextField(null=True)),
                ('vc_codEstado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('b_flagInactivo', models.BooleanField(db_column='b_flagInactivo')),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuarioCrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipCrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioEdita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipEdita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'General_Detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id_materiales', models.AutoField(primary_key=True, serialize=False)),
                ('vc_codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('vc_descripcion', models.CharField(max_length=200)),
                ('nu_valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('nu_stockMinimo', models.DecimalField(blank=True, db_column='nu_stockMinimo', decimal_places=2, max_digits=9, null=True)),
                ('nu_stockMaximo', models.DecimalField(blank=True, db_column='nu_stockMaximo', decimal_places=2, max_digits=9, null=True)),
                ('b_flagInactivo', models.BooleanField(db_column='b_flagInactivo')),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuarioCrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipCrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioEdita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipEdita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
                ('nu_stockActual', models.DecimalField(blank=True, db_column='nu_stockActual', decimal_places=2, max_digits=9, null=True)),
                ('vc_numNotificacion', models.CharField(blank=True, db_column='vc_numNotificacion', max_length=10, null=True)),
                ('vc_observacionDesaprobar', models.CharField(blank=True, db_column='vc_observacionDesaprobar', max_length=200, null=True)),
                ('id_statusAprobado', models.IntegerField(blank=True, db_column='id_statusAprobado', null=True)),
            ],
            options={
                'db_table': 'Materiales',
                'managed': False,
                'permissions': (('exportar_material', 'Exportar Materiales'), ('aprobar_material', 'Aprobar Material'), ('notificar_material', 'Notificar Material'), ('ver_material', 'Ve Material')),
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('vc_codestado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('vc_rucproveedor', models.CharField(db_column='vc_rucProveedor', max_length=11)),
                ('vc_razonsocial', models.CharField(db_column='vc_razonSocial', max_length=150)),
                ('vc_direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('vc_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('vc_telfcontacto', models.CharField(blank=True, db_column='vc_telfContacto', max_length=10, null=True)),
                ('vc_telfempresa', models.CharField(blank=True, db_column='vc_telfEmpresa', max_length=10, null=True)),
                ('b_flaginactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('vc_nombreProyecto', models.CharField(db_column='vc_nombreProyecto', max_length=120)),
                ('vc_direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('dt_fecAprobacion', models.DateField(blank=True, db_column='dt_fecAprobacion', null=True)),
                ('dt_fecInicio', models.DateField(blank=True, db_column='dt_fecInicio', null=True)),
                ('dt_fecCierre', models.DateField(blank=True, db_column='dt_fecCierre', null=True)),
                ('vc_nomContacto', models.CharField(blank=True, db_column='vc_nomContacto', max_length=120, null=True)),
                ('vc_telfContacto', models.CharField(blank=True, db_column='vc_telfContacto', max_length=10, null=True)),
                ('b_flagInactivo', models.BooleanField(db_column='b_flagInactivo')),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Proyectos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id_ubigeo', models.AutoField(primary_key=True, serialize=False)),
                ('vc_codigoubigeo', models.CharField(db_column='vc_codigoUbigeo', max_length=6)),
                ('vc_descripcion', models.CharField(max_length=50)),
                ('nu_totalprov', models.DecimalField(blank=True, db_column='nu_totalProv', decimal_places=0, max_digits=3, null=True)),
                ('nu_totaldist', models.DecimalField(blank=True, db_column='nu_totalDist', decimal_places=0, max_digits=3, null=True)),
                ('vc_descregion', models.CharField(blank=True, db_column='vc_descRegion', max_length=50, null=True)),
                ('vc_codestado', models.CharField(db_column='vc_codEstado', max_length=3)),
                ('b_flaginactivo', models.TextField(blank=True, db_column='b_flagInactivo', null=True)),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Ubigeo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id_unidadMedida', models.AutoField(db_column='id_unidadMedida', primary_key=True, serialize=False)),
                ('vc_descripcionlarga', models.CharField(db_column='vc_descripcionLarga', max_length=80)),
                ('vc_descripcionCorta', models.CharField(db_column='vc_descripcionCorta', max_length=5)),
                ('vc_codtipounidadmedida', models.CharField(db_column='vc_codTipoUnidadMedida', max_length=3)),
                ('nu_valor', models.FloatField()),
                ('nu_orden', models.DecimalField(decimal_places=0, max_digits=2)),
                ('b_flagInactivo', models.BooleanField(db_column='b_flagInactivo')),
                ('dt_crea', models.DateTimeField()),
                ('vc_usuariocrea', models.CharField(db_column='vc_usuarioCrea', max_length=50)),
                ('vc_ipcrea', models.CharField(db_column='vc_ipCrea', max_length=20)),
                ('dt_edita', models.DateTimeField(blank=True, null=True)),
                ('vc_usuarioedita', models.CharField(blank=True, db_column='vc_usuarioEdita', max_length=50, null=True)),
                ('vc_ipedita', models.CharField(blank=True, db_column='vc_ipEdita', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Unidad_Medida',
                'managed': False,
            },
        ),
    ]
