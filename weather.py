import urllib3, json, API, numpy

http = urllib3.PoolManager()
f = open("bajson.txt", "a")
inp = input("Type city to search it: ")
nearlat = http.request("GET", "http://api.weatherapi.com/v1/current.json?key=9d965cf9c7af4c8aabb132022201807&q=" + inp)
city = http.request("GET", "http://api.weatherapi.com/v1/forecast.json?key=9d965cf9c7af4c8aabb132022201807&q=" + inp)
baja = http.request("GET", "http://api.weatherapi.com/v1/forecast.json?key=9d965cf9c7af4c8aabb132022201807&q=Mostar")
array = json.loads(nearlat.data.decode('utf-8'))
city_location = array["location"]
lat = city_location["lat"]
lon = city_location["lon"]
# print(json.loads(city.data.decode('utf-8')))
loc = API.get_city(str(lat), str(lon))
print(type(loc))

""" callapinorth = API.get_city_array(str(lat + 1), str(lon))
callapieast = API.get_city_array(str(lat), str(lon + 1))
callapisouth = API.get_city_array(str(lat - 1), str(lon))
callapiwest = API.get_city_array(str(lat), str(lon - 1 ))
print("NORTH")
print(callapinorth["current"])
print("EAST")
print(callapieast["current"]["wind_dir"])
print("SOUTH")
print(callapisouth["current"]["wind_dir"])
print("WEST")
print(callapiwest["current"]["wind_dir"]) """

#Wind loops 
#NE
""" NE = []
print("GETTING DATA FOR LOCATIONS LAT: +-1 AND LON. +-1")
for i in numpy.arange(lat + 1, lat - 1, -0.1):
    for j in numpy.arange(lon - 1, lon + 1, 0.1):
        loc = API.get_city(str(i), str(j))
        print(type(loc))
        if hasattr(loc, "error"):
            pass
        else:
            NE.append(loc)
            f.write(str(loc))
            f.write("\n")
f.close() """