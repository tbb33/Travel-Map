import folium

#creating map object
map = folium.Map(location=[29.8884, -97.9384], zoom_start=6, tiles="Stamen Terrain")
#add marker - obj will be child
map.add_child(folium.Marker(location=[29.8884, -97.9384],
    popup="Texas State University", icon=folium.Icon(color='blue', icon='star') ))


map.save("Map1.html")
