from django.urls import path, re_path
from . import views

urlpatterns = [
    path(
        'sign-in/',
        views.SignInView.as_view(),
        name='sign-in'
    ),
    path(
        'sign-out/',
        views.SignOutView.as_view(),
        name='sign-out'
    ),
    re_path(
        r'^monitorear/(?P<id_invernadero>[0-9]+)/',
        views.monitorear_invernadero,
        name = 'monitorear'
    ),
    path(
        'monitorear/',
        views.monitorear_invernadero,
        name = 'monitorear'
    ),
    path(
        '',
        views.InvernaderosListView.as_view(),
        name='invernaderos'
    ),
    path(
        'cultivos/',
        views.CultivosListView.as_view(),
        name='cultivos'
    ),
    path(
        'dispositivos/',
        views.DispositivosListView.as_view(),
        name='dispositivos'
    ),
    path(
        'parametros/',
        views.ParametrosListView.as_view(),
        name='parametros'
    ),
    path(
        'sensores/',
        views.SensoresListView.as_view(),
        name='sensores'
    ),
    path(
        'actuadores/',
        views.ActuadoresListView.as_view(),
        name='actuadores'
    ),
    path(
        'detalle/invernadero/<slug:pk>/',
        views.InvernaderoDetailView.as_view(),
        name='invernadero-detalle'
    ),
    path(
        'detalle/dispositivo/<slug:pk>/',
        views.DispositivoDetailView.as_view(),
        name='dispositivo-detalle'
    ),
    path(
        'detalle/sensor/<slug:pk>/',
        views.SensorDetailView.as_view(),
        name='sensor-detalle'
    ),
    path(
        'detalle/actuador/<slug:pk>/',
        views.ActuadorDetailView.as_view(),
        name='actuador-detalle'
    ),
    path(
        'detalle/cultivo/<slug:pk>/',
        views.CultivoDetailView.as_view(),
        name='cultivo-detalle'
    ),
    path(
        'detalle/parametro/<slug:pk>/',
        views.ParametroDetailView.as_view(),
        name='parametro-detalle'
    ),
    path(
        'edicion/invernadero/<slug:pk>/',
        views.InvernaderoUpdateView.as_view(),
        name='invernadero-edicion'
    ),
    path(
        'edicion/dispositivo/<slug:pk>/',
        views.DispositivoUpdateView.as_view(),
        name='dispositivo-edicion'
    ),
    path(
        'edicion/sensor/<slug:pk>/',
        views.SensorUpdateView.as_view(),
        name='sensor-edicion'
    ),
    path(
        'edicion/actuador/<slug:pk>/',
        views.ActuadorUpdateView.as_view(),
        name='actuador-edicion'
    ),
    path(
        'edicion/cultivo/<slug:pk>/',
        views.CultivoUpdateView.as_view(),
        name='cultivo-edicion'
    ),
    path(
        'edicion/parametro/<slug:pk>/',
        views.ParametroUpdateView.as_view(),
        name='parametro-edicion'
    ),
    path(
        'crear/invernadero/',
        views.InvernaderoCreateView.as_view(),
        name='invernadero-crear'
    ),
    path(
        'crear/dispositivo/',
        views.DispositivoCreateView.as_view(),
        name='dispositivo-crear'
    ),
    path(
        'crear/sensor/',
        views.SensorCreateView.as_view(),
        name='sensor-crear'
    ),
    path(
        'crear/actuador/',
        views.ActuadorCreateView.as_view(),
        name='actuador-crear'
    ),
    path(
        'crear/cultivo/',
        views.CultivoCreateView.as_view(),
        name='cultivo-crear'
    ),
    path(
        'crear/parametro/',
        views.ParametroCreateView.as_view(),
        name='parametro-crear'
    ),
    re_path(
        r'ajax/invernadero/(?P<id_invernadero>[0-9]+)/',
        views.invernadero,
        name='ajax-invernadero'
    ),
    re_path(
        r'ajax/dispositivo/(?P<id_dispositivo>[0-9]+)/',
        views.dispositivo,
        name='ajax-dispositivo'
    ),
    re_path(
        r'ajax/sensor/(?P<id_sensor>[0-9]+)/',
        views.sensor,
        name='ajax-sensor'
    ),
    re_path(
        r'ajax/actuador/(?P<id_actuador>[0-9]+)/',
        views.actuador,
        name='ajax-actuador'
    ),
    re_path(
        r'ajax/cultivo/(?P<id_cultivo>[0-9]+)/',
        views.cultivo,
        name='ajax-cultivo'
    ),
    re_path(
        r'ajax/parametro/(?P<id_parametro>[0-9]+)/',
        views.parametro,
        name='ajax-parametro'
    ),
    re_path(
        r'$/perfil/<slug:pk>/',
        views.PerfilUpdateView.as_view(),
        name='perfil'
    )
]
