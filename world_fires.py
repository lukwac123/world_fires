from pathlib import Path
import csv

import plotly.express as px

path = Path('world_fires_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Pobranie danych o szerokości i długości oraz siły pożaru.
lats, lons, brights = [], [], []
for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        print(f"Brak danych dla {row[5]}.")
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Utworzenie mapy świata z pożarami.
title = 'Pożary na świecie w dniu 03.04.2022'
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights,
                     color_continuous_scale='reds',
                     labels={'color':'Siła'},
                     projection='natural earth'
                     )
fig.show()