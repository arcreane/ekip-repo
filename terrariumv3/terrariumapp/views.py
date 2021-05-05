from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.template import RequestContext
# from terrmodels import Person
from django.views.decorators.csrf import csrf_protect

from django import forms

from . import models, client_mqtt
from .models import mqtt_client
from .models.models import Person, Programme_eau, Programme_temperature, Capteur, Programme_oxygene


class PersonForm(forms.Form):
    firstname = forms.CharField(max_length=200, label="nom : ")
    lastname = forms.CharField(max_length=200, label="prenom : ")
    age = forms.IntegerField(label="age : ")


def index(request):
    return render(request, "index.html")


def home(request):
    if request.method == "POST":
        monFormulaire = PersonForm(request.POST)
        if monFormulaire.is_valid():
            return add(request, monFormulaire)
    else:
        monFormulaire = PersonForm()

    return render(request, "home.html", {"form": monFormulaire})


@csrf_protect
def add(request, formulaire, template_name="show_person.html"):
    args = {}
    moi = Person.objects.create(firstname="toto")
    moi.save()
    # moi.firstname = formulaire.cleaned_data["firstname"]
    # moi.lastname = formulaire.cleaned_data["lastname"]
    # moi.age = formulaire.cleaned_data["age"]
    args['person'] = moi

    return TemplateResponse(request, template_name, args)


global toto


def display(request, person_id, template_name="show_person.html"):
    args = {}
    args['id'] = person_id
    args['prenom'] = toto
    # moi = Person.objects.create(firstname = "jean machin", age = 18)
    # moi.save()
    moi = Person.objects.get(id=3)

    args['person'] = moi
    return TemplateResponse(request, template_name, args)


def get_eau():
    # print("je fais une requete mqtt")
    if type(models.mqtt_client.values) == type([]):
        return models.mqtt_client.values[-1]["humidite"]
    else:
        return 0


def get_temperature():
    # print("je fais une requete mqtt")
    return 15


def get_oxygen():
    # print("je fais une requete mqtt")
    return 15


sensors = {"eau": (get_eau, Programme_eau), "temperature": (get_temperature, Programme_temperature),
           "oxygene": (get_oxygen, Programme_oxygene)}


def all_sensor_infos(request, template_name="show_sensors.html"):
    args = {}
    capteurs = []
    for sensor in sensors.items():
        print(sensor)
        val = sensor[1][0]()
        capteur = Capteur(sensor[0], val, sensor[1][1](val))
        capteurs.append(capteur)

    args["mqtt"] = models.mqtt_client.values
    args["capteurs"] = capteurs
    return TemplateResponse(request, template_name, args)


def sensor_infos(request, capteur_type, template_name="show_sensor.html"):
    args = {}
    args['name'] = capteur_type

    val = sensors[capteur_type][0]()
    args['info'] = sensors[capteur_type][1](val)

    return TemplateResponse(request, template_name, args)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def change_mqtt_client_state(request, action):
    print(client_mqtt)
    if action == "stop":
        mqtt_client.stop()
    elif action == "start":
        mqtt_client.start()
    return all_sensor_infos(request)


toto = "Jean Truc"


