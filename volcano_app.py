#web map - volcanoes in US
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
html ="""<h5>Volcano Info:</h5>
Name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
Height: %s m"""

#function to color icon based on elevation
def iccolor(elv):
    if elv<1000 :
        result='green'
    elif elv>=1000 and elv <3000:
        result='orange'
    elif (elv >=3000):
        result='red'
    return result

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fgv=folium.FeatureGroup("Volcanoes")
fgp=folium.FeatureGroup("Population")

for lt, ln, el, nm in zip(lat,lon, elev, name):
    iframe = folium.IFrame(html = html % (nm, nm, el), width=200,height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=iccolor(el), icon='star')))

#add polygon layer; creates geoJson object; colors countries based on population
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding = 'utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
