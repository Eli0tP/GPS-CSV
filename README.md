# Visualisateur de parcours GPS

Mini-projet de NSI (lycée Saint-André, 2023) : visualisation et analyse d'un parcours de course à pied
à partir d'un relevé GPS au format CSV.

## Fonctionnalités

- Lecture d'un fichier CSV (heure, latitude, longitude, altitude, fréquence cardiaque)
- Tracé du parcours sur une carte interactive, cadrée automatiquement sur la zone de la course
- Calcul des distances entre points avec la **formule de Haversine**
- Curseur pour suivre le coureur point par point : temps, distance, vitesse, altitude, cardio,
  calories dépensées et intensité de l'effort
- Courbes d'altitude et de fréquence cardiaque sur toute la course

## Technologies

Python · Tkinter · [tkintermapview](https://github.com/TomSchimansky/TkinterMapView) · module `csv`

## Lancer le projet

```bash
pip install tkintermapview
python main.py
```

Le programme demande le nom du fichier à ouvrir : saisir `marathon_la_rochelle_2008.csv` ou
`coulee_verte_2018.csv` (deux parcours d'exemple fournis).

## Structure

| Fichier | Rôle |
|---|---|
| `main.py` | fenêtre principale et carte |
| `calcul.py` | lecture du CSV, bornes du parcours, formule de Haversine |
| `IHM_graphique.py` | marqueur de départ et tracé du parcours |
| `slider.py` | curseur et statistiques du coureur (vitesse, calories, intensité) |
| `graphique.py` | courbes d'altitude et de fréquence cardiaque |
