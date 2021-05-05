from django.db import models
import datetime
from django.utils import timezone


class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, default= "")
    age = models.IntegerField(default= 10)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Capteur:
    def __init__(self, name, value, info):
        self.name = name
        self.value = value
        self.info = info



    ## DEBUT DU BORDEL



from math import *


def Programme_eau(taux):
    global Erreur_eau
    global retablissement_eau
    # recuperer le taux d'humidité (en Lm-3)
    # taux = 40  # dans l'attente d'une vraie valeur
    Erreur_eau = 100*abs(taux-70)/70
    Erreur_eau = round(Erreur_eau)
    if Erreur_eau > 100:
        Erreur_eau = 100
    retablissement_eau = taux-70
    if retablissement_eau > 7:
        return "baissez le taux d'humidité"
    if retablissement_eau < -7:
        return "augmentez le taux d'humité"


def Programme_temperature(temperature):
    global Erreur_temperature
    global retablissement_temperature
    # recuperer la temperature (en °C)
    # temperature = 25  # dans l'attente d'une vraie valeur
    Erreur_temperature = 100*sqrt((temperature-21)**2)/21
    Erreur_temperature = round(Erreur_temperature)
    if Erreur_temperature > 100:
        Erreur_temperature = 100
    retablissement_temperature = temperature-21

    if retablissement_temperature > 2.5:
        return "baissez la temperature"
    elif retablissement_temperature < -2.5:
        return "augmentez la temperature"
    else:
        return "Touche a rien c'est parfait"


def Programme_oxygene(oxygene):
    global Erreur_oxygene
    global retablissement_oxygene
    # recuperer le taux d'oxygene (en Lm-3)
    # oxygene = 5  # dans l'attente d'une vraie valeur
    Erreur_oxygene = 100*sqrt((oxygene-18)**2)/18
    Erreur_oxygene = round(Erreur_oxygene)
    if Erreur_oxygene > 100:
        Erreur_oxygene = 100
    retablissement_oxygene = oxygene-18
    if retablissement_oxygene > 1.8:
        return "baissez le taux d'oxygene"
    if retablissement_oxygene < -1.8:
        return "augmentez le taux d'oxygene"
    if -1.8 < retablissement_oxygene < 1.8:
        return "le taux d'oxygene est normal"


def Programme_lumiere():
    global Erreur_lumiere
    global retablissement_luminosité
    luminosite = 7000  # dans l'attente d'une vraie valeur
    # recuperer la luminosité (en lux)
    Erreur_lumiere = 100*sqrt((luminosite-7750)**2)/7750
    Erreur_lumiere = round(Erreur_lumiere)
    if Erreur_lumiere > 100:
        Erreur_lumiere = 100
    retablissement_luminosité = luminosite-7750



class Persons():
    def __init__(self, namePerson, prenamePerson, agePerson):
        self.namePerson = namePerson
        self.prenamePerson = prenamePerson
        self.agePerson = agePerson



# corps du programme principal
#
# Joie = 100 - (Erreur_eau + Erreur_lumiere +
#               Erreur_oxygene + Erreur_temperature)/4
# Joie = round(Joie)
# print("l'erreur d'eau est de ", Erreur_eau, "%")
# if retablissement_eau > 7:
#     print("baissez le taux d'humidité")
# if retablissement_eau < -7:
#     print("augmentez le taux d'humité")
# if -7 < retablissement_eau < 7:
#     print("le taux d'humidité est normal")
# print("l'erreur de lumiere est de ", Erreur_lumiere, "%")
# if retablissement_luminosité > 775:
#     print("baissez la luminosité")
# if retablissement_luminosité < -775:
#     print("augmentez la luminosité")
# if -775 < retablissement_luminosité < 775:
#     print("la luminosité est normale")
# print("l'erreur d'oxygene est de ", Erreur_oxygene, "%")
# if retablissement_oxygene > 1.8:
#     print("baissez le taux d'oxygene")
# if retablissement_oxygene < -1.8:
#     print("augmentez le taux d'oxygene")
# if -1.8 < retablissement_oxygene < 1.8:
#     print("le taux d'oxygene est normal")
# print("l'erreur de temperature est de ", Erreur_temperature, "%")
# if retablissement_temperature > 2.5:
#     print("baissez la temperature")
# if retablissement_temperature < -2.5:
#     print("augmentez la temperature")
# if -2.5 < retablissement_temperature < 2.5:
#     print("la temperature est normale")
# print("votre score de joie est de ", Joie, "pts")
