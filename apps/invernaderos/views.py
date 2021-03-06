from django.views.generic import CreateView, TemplateView 
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone

from .forms import LoginForm, UserUpdateForm, InvernaderoForm
from .models import *

import json

class SignUpView(LoginRequiredMixin, CreateView):
    model = User
    form_class = LoginForm


class SignInView(LoginView):
    template_name = 'invernaderos/iniciarSesion.html'

    
"""class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'invernaderos/iniciarSesion.html'
    success_url = reverse_lazy('invernaderos:invernaderos')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(self, Login).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(self, Login).form_valid(form)
"""

class SignOutView(LoginRequiredMixin, LogoutView):
    template_name = 'invernaderos/iniciarSesion.html'


class InvernaderosListView(LoginRequiredMixin, ListView):
    model = Invernadero
    template_name = 'invernaderos/gestionarInvernaderos.html'
    context_object_name = 'invernaderos'


    def get_queryset(self):
        user = self.request.user
        context = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        return context
    
    def get_context_data(self, **kwargs):
        context = super(InvernaderosListView, self).get_context_data(**kwargs)
        return context


class CultivosListView(LoginRequiredMixin, ListView):
    model = Cultivo
    template_name = 'invernaderos/gestionarCultivos.html'
    context_object_name = 'cultivos'


    def get_queryset(self):
        user = self.request.user
        context = Cultivo.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        return context
    
    def get_context_data(self, **kwargs):
        context = super(CultivosListView, self).get_context_data(**kwargs)
        return context


class ParametrosListView(LoginRequiredMixin, ListView):
    model = Parametro
    template_name = 'invernaderos/gestionarParametros.html'
    context_object_name = 'parametros'


    def get_queryset(self):
        user = self.request.user
        invernaderos = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        parametros = Parametro.objects.all().filter(is_baja=False)
        datos = []
        for invernadero in invernaderos:
            result = parametros.filter(id_invernadero=invernadero.id_invernadero)
            for parametro in result:
                datos.append(parametro)
        context = datos
        return context
    
    def get_context_data(self, **kwargs):
        context = super(ParametrosListView, self).get_context_data(**kwargs)
        return context


class DispositivosListView(LoginRequiredMixin, ListView):
    model = Dispositivo
    template_name = 'invernaderos/gestionarDispositivos.html'
    context_object_name = 'dispositivos'


    def get_queryset(self):
        user = self.request.user
        dispositivos = Dispositivo.objects.all().filter(is_baja=False)
        invernaderos = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        datos = []
        for invernadero in invernaderos:
            if invernadero.id_dispositivo in dispositivos:
                if not invernadero.id_dispositivo in datos:
                    datos.append(invernadero.id_dispositivo)
        context = datos
        return context
    
    def get_context_data(self, **kwargs):
        context = super(DispositivosListView, self).get_context_data(**kwargs)
        return context


class SensoresListView(LoginRequiredMixin, ListView):
    model = Sensor
    template_name = 'invernaderos/gestionarSensores.html'
    context_object_name = 'sensores'


    def get_queryset(self):
        user = self.request.user
        sensores = Sensor.objects.all().filter(is_baja=False)
        invernaderos = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        datos = []
        for invernadero in invernaderos:
            result = sensores.filter(id_invernadero=invernadero.id_invernadero)
            for sensor in result:
                datos.append(sensor)
        context = datos
        return context
    
    def get_context_data(self, **kwargs):
        context = super(SensoresListView, self).get_context_data(**kwargs)
        return context


class ActuadoresListView(LoginRequiredMixin, ListView):
    model = Actuador
    template_name = 'invernaderos/gestionarActuadores.html'
    context_object_name = 'actuadores'


    def get_queryset(self):
        user = self.request.user
        invernaderos = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
        actuadores = Actuador.objects.all().filter(is_baja=False)
        datos = []
        for invernadero in invernaderos:
            result = actuadores.filter(id_invernadero=invernadero.id_invernadero)
            for actuador in result:
                datos.append(actuador)
        context = datos
        return context
    
    def get_context_data(self, **kwargs):
        context = super(ActuadoresListView, self).get_context_data(**kwargs)
        return context


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'invernaderos/editForm.html'
    success_url = '/'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'date_joined'
    ]


class InvernaderoUpdateView(LoginRequiredMixin, UpdateView):
    model = Invernadero
    template_name = 'invernaderos/editForm.html'
    success_url = '/'
    fields = [
        'id_invernadero',
        'id_dispositivo',
        'id_cultivo',
        'nombre_invernadero',
        'ubicacion'
    ]


class ParametroUpdateView(LoginRequiredMixin, UpdateView):
    model = Parametro
    template_name = 'invernaderos/editForm.html'
    success_url = '/parametros/'
    fields = [
        'id_invernadero',
        'nombre_parametro',
        'magnitud_referencia_limite_inferior',
        'magnitud_referencia_limite_superior'    ]


class ActuadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Actuador
    template_name = 'invernaderos/editForm.html'
    success_url = '/actuadores/'
    fields = [
        'id_dispositivo',
        'id_invernadero',
        'nombre_actuador'
    ]


class SensorUpdateView(LoginRequiredMixin, UpdateView):
    model = Sensor
    template_name = 'invernaderos/editForm.html'
    success_url = '/sensores/'
    fields = [
        'id_dispositivo',
        'id_invernadero',
        'nombre_sensor'
    ]


class DispositivoUpdateView(LoginRequiredMixin, UpdateView):
    model = Dispositivo
    template_name = 'invernaderos/editForm.html'
    success_url = '/dispositivos/'
    fields = [
        'nombre_dispositivo'
    ]


class CultivoUpdateView(LoginRequiredMixin, UpdateView):
    model = Cultivo
    template_name = 'invernaderos/editForm.html'
    success_url = '/cultivos/'
    fields = [
        'nombre_cultivo',
        'periodo_cosecha'
    ]

class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'invernaderos/viewPerfil.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'date_joined',
        'last_login'
    ]
    context_object_name = 'user'


class InvernaderoDetailView(LoginRequiredMixin, DetailView):
    model = Invernadero
    template_name = 'invernaderos/viewInvernadero.html'
    fields = [
        'id_invernadero',
        'id_dispositivo',
        'id_usuario',
        'id_cultivo',
        'nombre_invernadero',
        'ubicacion'
    ]
    context_object_name = 'invernadero'


class ParametroDetailView(LoginRequiredMixin, DetailView):
    model = Parametro
    template_name = 'invernaderos/viewParametro.html'
    fields = [
        'id_parametro',
        'id_invernadero',
        'nombre_parametro',
        'magnitud_referencia_limite_inferior',
        'magnitud_referencia_limite_superior'
    ]


class ActuadorDetailView(LoginRequiredMixin, DetailView):
    model = Actuador
    template_name = 'invernaderos/viewActuador.html'
    fields = [
        'id_actuador',
        'id_dispositivo',
        'id_invernadero',
        'nombre_actuador'
    ]
    context_object_name = 'actuador'

class SensorDetailView(LoginRequiredMixin, DetailView):
    model = Sensor
    template_name = 'invernaderos/viewSensor.html'
    fields = [
        'id_sensor',
        'id_dispositivo',
        'id_invernadero',
        'nombre_sensor'
    ]
    context_object_name = 'sensor'


class DispositivoDetailView(LoginRequiredMixin, DetailView):
    model = Dispositivo
    template_name = 'invernaderos/viewDispositivo.html'
    fields = [
        'id_dispositivo',
        'nombre_dispositivo'
    ]
    context_object_name = 'dispositivo'


class CultivoDetailView(LoginRequiredMixin, DetailView):
    model = Cultivo
    template_name = 'invernaderos/viewCultivo.html'
    fields = [
        'id_cultivo',
        'nombre_cultivo',
        'periodo_cosecha'
    ]


class InvernaderoCreateView(LoginRequiredMixin, CreateView):
    model = Invernadero
    template_name = 'invernaderos/editForm.html'
    success_url = '/'
    fields = [
        'id_dispositivo',
        'id_cultivo',
        'nombre_invernadero',
        'ubicacion'
    ]
    
    def form_valid(self, form):
        invernadero = form.save()
        invernadero.id_usuario = self.request.user
        return super(InvernaderoCreateView, self).form_valid(form)  


class ParametroCreateView(LoginRequiredMixin, CreateView):
    model = Parametro
    template_name = 'invernaderos/editForm.html'
    success_url = '/parametros/'
    fields = [
        'id_invernadero',
        'nombre_parametro',
        'magnitud_referencialimite_inferior',
        'magnitud_referencia_limite_superior'
    ]


class ActuadorCreateView(LoginRequiredMixin, CreateView):
    model = Actuador
    success_url = '/actuadores/'
    template_name = 'invernaderos/editForm.html'
    fields = [
        'id_dispositivo',
        'id_invernadero',
        'nombre_actuador'
    ]


class SensorCreateView(LoginRequiredMixin, CreateView):
    model = Sensor
    success_url = '/sensores/'
    template_name = 'invernaderos/editForm.html'
    fields = [
        'id_dispositivo',
        'id_invernadero',
        'nombre_sensor'
    ]


class DispositivoCreateView(LoginRequiredMixin, CreateView):
    model = Dispositivo
    success_url = '/dispositivos/'
    template_name = 'invernaderos/editForm.html'
    fields = [
        'nombre_dispositivo'
    ]


class CultivoCreateView(LoginRequiredMixin, CreateView):
    model = Cultivo
    success_url = '/cultivos/'
    template_name = 'invernaderos/editForm.html'
    fields = [
        'nombre_cultivo',
        'periodo_cosecha'
    ]


@login_required()
def monitorear_invernadero(request, id_invernadero):
    if request.method == 'GET':
        data = Invernadero.objects.filter(id_invernadero=id_invernadero).filter(is_baja=False).exists()
        if data:
            user = request.user
            invernaderos = Invernadero.objects.all().filter(id_usuario=user.id).filter(is_baja=False)
            cant_invernaderos = invernaderos.count()

            datos = []
            dispositivos = Dispositivo.objects.all().filter(is_baja=False)
            for invernadero in invernaderos:
                if invernadero.id_dispositivo in dispositivos:
                    if not invernadero.id_dispositivo in datos:
                        datos.append(invernadero.id_dispositivo)
            cant_dispositivos = len(datos)
            
            actuadores = Actuador.objects.all().filter(is_baja=False)
            datos = []
            for invernadero in invernaderos:
                result = actuadores.filter(id_invernadero=invernadero.id_invernadero)
                for actuador in result:
                    datos.append(actuador)
            cant_actuadores = len(datos)

            sensores = Sensor.objects.all().filter(is_baja=False)
            datos = []
            for invernadero in invernaderos:
                result = sensores.filter(id_invernadero=invernadero.id_invernadero)
                for sensor in result:
                    datos.append(sensor)
            cant_sensores = len(datos)

            parametros = Parametro.objects.all().filter(is_baja=False)
            for invernadero in invernaderos:
                result = parametros.filter(id_invernadero=invernadero.id_invernadero)
                for parametro in result:
                    datos.append(parametro)

            cant_parametros = len(datos)
                
            cant_cultivos = Cultivo.objects.all().filter(id_usuario=user.id).filter(is_baja=False).count()

            data = get_data(id_invernadero)
            
            fecha = timezone.now()

            depure = depure_data(data)
                
            context = {
                'cant_cultivos': cant_cultivos,
                'cant_parametros': cant_parametros,
                'cant_sensores': cant_sensores,
                'cant_actuadores': cant_actuadores,
                'cant_dispositivos': cant_dispositivos,
                'cant_invernaderos': cant_invernaderos,
                'fecha': fecha,
                'id_invernadero': id_invernadero,
                'suelo_magnitud': depure['suelo_magnitud'],
                'suelo_fecha': depure['suelo_fecha'],
                'humedades_suelo': data['humedades_suelo'],
                'relativas_magnitud': depure['relativas_magnitud'],
                'relativas_fecha': depure['relativas_fecha'],
                'humedades_relativas': data['humedades_relativas'],
                'temperaturas': data['temperaturas'],
                'temp_magnitud': depure['temp_magnitud'],
                'temp_fecha': depure['temp_fecha']
            }

            temp = loader.get_template('invernaderos/monitorearInvernaderos.html')
            
            return HttpResponse(temp.render(context, request))
        else:
            temp = loader.get_template('404.html')
            return HttpResponse(temp.render({}, request))


def get_data(id_invernadero):            
    data = {}
            
    parametros = Parametro.objects.filter(id_invernadero=id_invernadero)

    for parametro in parametros:
        if parametro.nombre_parametro.upper() == 'HUMEDAD DEL AIRE':
            humedades_relativas = Medicion.objects.all().filter(id_invernadero=id_invernadero).filter(id_parametro = parametro.id_parametro)[:20]
            data['humedades_relativas'] = humedades_relativas
        elif parametro.nombre_parametro.upper() == 'HUMEDAD DEL SUELO':
            humedades_suelo = Medicion.objects.all().filter(id_invernadero=id_invernadero).filter(id_parametro = parametro.id_parametro)[:20]
            data['humedades_suelo'] = humedades_suelo
        elif parametro.nombre_parametro.upper() == 'TEMPERATURA':
            temperaturas = Medicion.objects.all().filter(id_invernadero=id_invernadero).filter(id_parametro = parametro.id_parametro)[:20]
            data['temperaturas'] = temperaturas
    return data

def depure_data(data):
    depure = {
        'relativas_magnitud': [],
        'relativas_fecha': [],
        'suelo_magnitud': [],
        'suelo_fecha': [],
        'temp_magnitud': [],
        'temp_fecha': []
    }

    for humedad_relativa in data['humedades_relativas']:
        depure['relativas_magnitud'].append(float(humedad_relativa.magnitud_medicion))
        depure['relativas_fecha'].append(str(humedad_relativa.fecha_medicion.strftime('%d/%m/%y %H:%M:%S')))
    
    for humedad_suelo in data['humedades_suelo']:
        depure['suelo_magnitud'].append(float(humedad_suelo.magnitud_medicion))
        depure['suelo_fecha'].append(str(humedad_suelo.fecha_medicion.strftime('%d/%m/%y %H:%M:%S')))
    
    for temp in data['temperaturas']:
        depure['temp_magnitud'].append(float(temp.magnitud_medicion))
        depure['temp_fecha'].append(str(temp.fecha_medicion.strftime('%d/%m/%y %H:%M:%S')))

    return depure

@login_required(login_url='/sign-in/')
def send_data(request):
    id_invernadero = request.GET['id_invernadero']
    fecha = timezone.now()
    data = get_data(id_invernadero)
    depure = depure_data(data)
    context = {
        'fecha': fecha,
        'suelo_magnitud': depure['suelo_magnitud'],
        'suelo_fecha': depure['suelo_fecha'],
        'relativas_magnitud': depure['relativas_magnitud'],
        'relativas_fecha': depure['relativas_fecha'],
        'temp_magnitud': depure['temp_magnitud'],
        'temp_fecha': depure['temp_fecha']
    }
            
    return JsonResponse(data=context)

@login_required(login_url='/sign-in/')
def invernadero(request, id_invernadero):  
    if request.method == 'DELETE':
        #id_invernadero = request.GET['identificador']
        invernadero = Invernadero.objects.get(id_invernadero=id_invernadero)
        invernadero.is_baja = True
        invernadero.save()
        message = "El invernadero fue borrado exitosamente"
        return JsonResponse(data={'message':message})

@login_required(login_url='/sign-in/')
def dispositivo(request, id_dispositivo):
    if request.method == 'DELETE':
        #id_dispositivo = request.POST['id']
        dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
        dispositivo.is_baja = True
        dispositivo.save()
        message = "El dispositivo fue borrado exitosamente"
        return JsonResponse(data={'message': message})        

@login_required(login_url='/sign-in/')
def sensor(request, id_sensor):
    if request.method == 'DELETE':
        #id_sensor = request.POST['id']
        sensor = Sensor.objects.get(id_sensor=id_sensor)
        sensor.is_baja = True
        sensor.save()
        message = "El sensor fue borrado exitosamente"
        return JsonResponse(data={'message': message})

@login_required(login_url='/sign-in/')
def actuador(request, id_actuador):  
    if request.method == 'DELETE':
        #id_actuador = request.POST['id']
        actuador = Actuador.objects.get(id_actuador=id_actuador)
        actuador.is_baja = True
        actuador.save()
        message = "El actuador fue borrado exitosamente"
        return JsonResponse(data={'message': message})

@login_required(login_url='/sign-in/')
def cultivo(request, id_cultivo):
    if request.method == 'DELETE':
        #id_cultivo = request.POST['id']
        cultivo = Cultivo.objects.get(id_cultivo=id_cultivo)
        cultivo.is_baja = True
        cultivo.save()
        message = "El cultivo fue borrado exitosamente"
        return JsonResponse(data={'message': message})

@login_required(login_url='/sign-in/')
def parametro(request, parametro):   
    if request.method == 'DELETE':
        #id_parametro = request.POST['id']
        parametro = Parametro.objects.get(id_parametro=id_parametro)
        parametro.is_baja = True
        parametro.save()
        message = "El parametro fue borrado exitosamente"
        return JsonResponse(data={'message': message})
