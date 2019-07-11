import folium
import pandas
d=pandas.read_csv("ECD.txt")
la=list(d["lat"])
lo=list(d["lon"])
el=list(d["Name"])
m1=folium.Map(location=[28.7041,77.1025],zoom_start=9)
f=folium.FeatureGroup(name="Colleges")
for i,j,k in zip(la,lo,el):
    f.add_child(folium.Marker(location=[i,j],popup=str(k),icon=folium.Icon(color='red')))

f1=folium.FeatureGroup(name="Population")
f1.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green'} ))
m1.add_child(f)
m1.add_child(f1)
m1.add_child(folium.LayerControl())
m1.save("Map1.html")
