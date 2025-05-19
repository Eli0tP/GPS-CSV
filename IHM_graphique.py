# ce programme sert a initialiser l'ihm graphique du projet

import calcul
from calcul import liste

# creation du marker au Debut de la course et du tracé du parcours
def ihm_graphique(map_widget):
    map_widget.set_marker(float(calcul.latitude_debut), float(calcul.longitude_debut)\
                          , text='Début')
    for i in range(1,len(liste)):
    # print(i, liste[i][-1])
        if i != 1:
            map_widget.set_path(position_list=[(float(liste[i-1][1]), float(liste[i-1][2]))\
                ,(float(liste[i][1]), float(liste[i][2]))], width= 2)
