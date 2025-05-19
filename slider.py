# ce programme contient toutes les definitions qui sont utilisées pour le texte du slider
# il definit également ce slider qui s'affiche tout au long du parcours

from tkinter import *
import calcul
from calcul import liste

# calcul de l'intensite du coureur
def intensite(position):
    FCmax = 220 - 40    #40 = l'age du coureur
    intensite = int(liste[position][-1]) / FCmax
    return round(intensite * 100,2)

# calcul de la depense de calories du coureur
def calcul_calories(position):
    calories = distance(position)* 65 * 1.036   #65 = poids du coureur
    return round(calories,2)

# calcul du temps en seconde pour l'utiliser dans le calcul de la vitesse
def convertit_temps_seconde(position):
    temps_debut = liste[1][0].split(':')
    temps_voulue = liste[position][0].split(':')
    heure = int(temps_voulue[0]) - int(temps_debut[0])
    minutes = int(temps_voulue[1]) - int(temps_debut[1])
    secondes = int(temps_voulue[2]) - int(temps_debut[2])
    temps_totale = heure*3600 + minutes*60 + secondes
    return temps_totale

# calcul de la vitesse du coureur
def vitesse(position):
    if distance(position) >= 0.01:
        vitesse = (distance(position)*1000)/float(convertit_temps_seconde(position)/3.6)
        return round(vitesse,2)

# calcul de la distance parcourue par le coureur
def distance(position):
    distance = 0
    for i in range(1,position):
        if i != 1:
            distance = calcul.distance_entre_point(liste[i-1][1], liste[i-1][2],\
                                           liste[i][1], liste[i][2]) + distance
    return round(distance,3)

# cette def fait bouger le marker a la position du slider avec les informations du coureur
def move_point(position, marker3):
    if position == 0:
        marker3.set_position(float(liste[1][1]), float(liste[1][2]))
    else:
        marker3.set_position( float(liste[position][1]),float(liste[position][2]))
        text_course = 'temps:' + liste[position][0] + "\n"\
                      +'cardio :' + liste[position][-1] +' BPM'+ "\n"\
                      + 'Altitude :' + liste[position][3] + ' M'+ "\n"\
                      +'Distance :' + str(distance(position))+ ' Kms' + "\n"\
                      + 'Vitesse :' + str(vitesse(position))+ ' Km/h' + "\n"\
                      + 'Calories :' + str(calcul_calories(position)) + 'Kcal' + "\n"\
                      +'Intensite :' + str(intensite(position)) + '%'
        # print(text_course)
        marker3.set_text(text_course)

# definition regroupent tous pour pouvoir l'appeler quand le slider bouge
def slider_position(position, marker3,root_tk):
    position_slider = int(position)
    move_point(position_slider, marker3)


# creation du slider plus appele de la fonction slider_position
def slider(root_tk, map_widget, marker3):
    slider = Scale(root_tk, from_=0, to=len(liste)-1, orient=HORIZONTAL\
                   , command=lambda position: slider_position(position, marker3, root_tk))
    slider.pack(side="top", fill='x')