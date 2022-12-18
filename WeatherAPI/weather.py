import json
import requests

myfile =  open(r"WeatherAPI\secrets.json",'r')
json_data = json.load(myfile)

seckey = json_data["WeatherAPI"]["secretkey"]
city = input("Please Enter the City Name to get Weather Conditions ")
response = requests.get("http://api.weatherstack.com/current?access_key={}&query={}&units=m".format(seckey, city))
res_json = response.json()
#print(res_json)

temp = res_json["current"]["temperature"]
desc = res_json["current"]["weather_descriptions"]
hum = res_json["current"]["humidity"]
country = res_json["location"]["country"]
lat = res_json["location"]["lat"]
lon = res_json["location"]["lon"]
localtime = res_json["location"]["localtime"]
press = res_json["current"]["pressure"]
precip = res_json["current"]["precip"]
uv_index = res_json["current"]["uv_index"]


print("------- Welcome to Weather Conditions ------")
print("City Name: {}, Country: {}".format(city, country))
print("Latitude: {}, Longitude: {}, Localtime: {}".format(lat, lon, localtime))
print("Temperature: {}".format(temp))
print("Description: {}".format(desc))
print("Pressure: {}".format(press))
print("Precipitation: {}".format(precip))
print("UV Index: {}".format(uv_index))
print("------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXX ------")
