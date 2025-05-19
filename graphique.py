# ce programme contient les definitions des différents graphes du projet

from tkinter import *
from calcul import liste
from slider import vitesse

def ratio():
    n = len(liste)
    ratio = n / 1250    # ce que peux afficher le graphique sur un seul ecran
    return round(ratio,0)
print(ratio(), 'ratio')

# creation du graphique qui represente la varition de l'altitude tout au long du parcours
def graphique_atlitude(root_tk):
    graphique1 = Canvas(root_tk,height=50)
    graphique1.create_text(110, 40, text="courbe de l'altitude au cours de la course",fill='blue')
    graphique1.create_text(20, 30, text= liste[1][3] + ' m', fill='blue')
    graphique1.create_text(1250, 30, text= liste[-1][3] + ' m', fill='blue')
    for i in range(int(ratio()),len(liste)):
        x1 = round((i-1)/ratio(),0)
        y1 = (liste[int(x1)][3])
        x2 = round((i)/ratio(),0)
        y2 = (liste[int(x2)][3])
        graphique1.create_line(x1, y1, x2, y2, fill='blue')
    graphique1.pack(side="bottom",fill='x')

# creation du graphique qui represente la varition du cardio tout au long du parcours
def graphique_cardio(root_tk):
    graphique2 = Canvas(root_tk, height=95)
    graphique2.create_text(110, 40, text="courbe du cardio au cours de la course", fill='red')
    graphique2.create_text(30,20, text= liste[1][-1] + ' BPM' ,fill='red')
    graphique2.create_text(1250,60, text= liste[-1][-1] + ' BPM', fill='red')
    for i in range(int(ratio()), len(liste)):
        x1 = round((i - 1)/ratio(),0)
        y1 = int(liste[int(x1)][4])/2           #on divise par deux pour diminuer l'echelle du cardio
        x2 = round(i/ratio(),0)
        y2 = int(liste[int(x2)][4])/2
        graphique2.create_line(x1, y1, x2, y2, fill='red')
    graphique2.pack(side="bottom", fill='x')
