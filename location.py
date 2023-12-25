import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "ger")  #ger for German language to display
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)  #service provider number and name
print(carrier.name_for_number(service_pro, "ger"))

from opencage.geocoder import OpenCageGeocode

key = 'API Key'  #paste API Key but for safety reason I removed it

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat'] #alternative way to show exact location is to consider using latitude and length
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("mylocation.html")