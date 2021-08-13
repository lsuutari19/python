import folium
import pandas


data = pandas.read_csv("data/volcanoes.txt")
fgvol = folium.FeatureGroup(name = "Volcanoes")
fgpop = folium.FeatureGroup(name = "Population")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])


def elevation_colors(elevation):
        if elevation >= 3000:
            return "black"
        elif 2000 <= elevation < 3000:
            return "red"
        elif  1500 <= elevation < 2500:
            return "orange"
        else:
            return "green"


for lat,long,elev,nam in zip(latitude, longitude, elevation, name):
    fgvol.add_child( folium.CircleMarker( location = [lat, long], radius = 10, popup = str(elev) + "m", tooltip = nam,
     fill_color= elevation_colors(elev), fill_opacity= 0.5, fill=True, color = "grey") ) 

fgpop.add_child(folium.GeoJson(data=open('data/world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005']<10000000 else
    'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map = folium.Map(location = [35.22, -108.22], zoom_start=8, tiles = "Stamen Terrain")



map.add_child(fgvol)
map.add_child(fgpop)
map.add_child( folium.LayerControl() )

map.save("Map1.html")

