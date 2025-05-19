"""
Lycée Saint-André :: 1NSI
Mini-projet : GPS/CSV
Pechadre Eliot
04/2023
"""

# le main est le programme python principal de mon projet
# il sert a appeler les differents autres programmes pour plus de comprehension

import IHM_graphique
import graphique
import slider
import tkinter
from tkinter import *
import tkintermapview
import calcul
from calcul import *

# creation de la fenetre et zoom sur le lieu de la course
root_tk = Tk()
root_tk.geometry(f"{1600}x{1000}")
root_tk.title("map de votre circuit")
map_widget = tkintermapview.TkinterMapView(root_tk, width=1600, height=760, corner_radius=0,)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.fit_bounding_box((calcul.latitude_max(), calcul.longitude_min()) \
                            , (calcul.latitude_min(), calcul.longitude_max()))  # La Rochelle

# creation du marker au debut et du trace du parcours
IHM_graphique.ihm_graphique(map_widget)

# creation du marker qui se deplacera sur le circuit grâce a la fonction slider
marker3 = map_widget.set_marker(float(liste[1][1]), float(liste[1][2]))
slider.slider(root_tk, map_widget, marker3)

# ajout des graphiques
graphique.graphique_atlitude(root_tk)
graphique.graphique_cardio(root_tk)

# lancement du programme
root_tk.mainloop()


