from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    url(r'^proyectos$', views.proyectos, name='proyectos'),
    url(r'^nuevo/proyecto$', views.post_nuevoMantenimiento, name="nuevo_mant"),
    url(r'^buscarNumDocumento$', views.buscarNumDocumento, name='busca_documento'),
    url(r'^exportar/proyecto$', views.exportarProyectos, name='exportar_proyectos'),
    url(r'^guardar/proyecto$', views.guardarProyecto, name='guardar_proyecto'),
    url(r'^editar/proyecto/(?P<idProyecto>\d+)/(?P<idVista>\d+)/$', views.editarProyecto, name='editar_proyecto'),
    url(r'^editar/proyecto$', views.guardarEditarProyecto, name='guardar_editar_proyecto'),
    url(r'^estatusProyecto$', views.estatusProyecto, name='estatus_proyecto'),

    url(r'^materiales$', permission_required('mantenimiento.view_materiales')(views.materiales), name='materiales'),
    url(r'^nuevo/material$', permission_required('mantenimiento.add_materiales')(views.MaterialesCreateView.as_view()),
        name='index'),
    url(r'^editar/material/(?P<pk>[0-9]+)/(?P<tipo>\d+)$',
        permission_required('mantenimiento.change_materiales')(views.MaterialesUpdateView.as_view()),
        name='editar_material'),
    url(r'^buscarMateriales$', views.buscarMateriales, name='buscar_materiales'),
    url(r'^exportar/materiales/(?P<search>[a-zA-Z0-9]+)/$', views.exportarMateriales, name='exportar_materiales'),
    url(r'^activar/material/(?P<idMaterial>\d+)$', views.activeMaterial, name='activar_material'),
    url(r'^desactivar/material/(?P<idMaterial>\d+)$', views.desactiveMaterial, name='desactivar_material'),
    url(r'^notificar/material$', views.viewNotificar, name="view_notificar"),
    url(r'^notificar/materiales$', views.notificarMaterial, name="notificar_material"),
    url(r'^aprobar/material$', views.viewAprobar, name="view_aprobar"),
    url(r'^aprobar/materiales/(?P<idMaterial>\d+)$', views.aprobarMaterial, name="aprobar_material"),
    url(r'^verificar/(?P<idMaterial>\d+)$', views.verificar, name="verificar"),
    url(r'^buscarAprobados$', views.buscarAprobados, name='buscar_aprobados'),
    url(r'^desaprobar/(?P<idMaterial>\d+)$', views.desaprobarMaterial, name='desaprobar_material'),
    url(r'^notificar/aprobado$', views.viewNotificarAprobados, name="view_notificar_aprobados"),
    url(r'^generarCodigo$', views.generarCodigo, name="generar_codigo"),

]
