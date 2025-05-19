# ce programme sert principalement a effectuer des calculs
# il est appelé par les autres programmes et renvoie des valeurs

import csv

# vu que j'ouvre le dossier csv qu'ici je demande a l'utilisateur quel dossier veut-il ouvrir
def dossier_demander():
    dossier_demander = input("Quel dossier csv voulez-vous ouvrir ? \n PS: n'oubliez pas le .csv")
    return dossier_demander
liste = []
with open(dossier_demander()) as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        liste.append(row)

# calcul des longitudes max et min et des latitudes max et min pour le fit.bouxing.box
def longitude_min():
    min_longitude = 90
    for i in range(1, len(liste)):
        if float(liste[i][2]) < min_longitude:
            min_longitude = float(liste[i][2])
    return min_longitude
def longitude_max():
    max_longitude = -90
    for i in range(1, len(liste)):
        if float(liste[i][2]) > max_longitude:
            max_longitude = float(liste[i][2])
    return max_longitude

def latitude_min():
    min_latitude = 90
    for i in range(1, len(liste)):
        if float(liste[i][1]) < min_latitude:
            min_latitude = float(liste[i][1])
    return  min_latitude
def latitude_max():
    max_latitude = -90
    for i in range(1, len(liste)):
        if float(liste[i][1]) > max_latitude:
            max_latitude = float(liste[i][1])
    return max_latitude

longitude_debut = liste[1][2]
longitude_fin= liste[-1][2]
latitude_debut = liste[1][1]
latitude_fin = liste[-1][1]

import math

# calcul de la distance entre deux points
def distance_entre_point(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    R = 6371  # rayon de la Terre en km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# calcul de la distance totale pour comparer a la realité
distance_totale = 0
for i in range(1,len(liste)):
    if i != 1:
        distance_totale += distance_entre_point(float(liste[i-1][1]), float(liste[i-1][2])\
                                                , float(liste[i][1]), float(liste[i][2]) )
#  print('la distance du parcours est de ',distance_totale, 'en km')