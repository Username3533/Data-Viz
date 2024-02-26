import json

import plotly.graph_objs as go
from plotly.offline import plot

filename = './eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

""" readable_file = './readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) """

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)



data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
    }]
layout = go.Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': layout}
plot(fig, filename='global_earthquakes.html')
