import urllib3, json

http = urllib3.PoolManager()
def get_city (lat,lon):
    array = http.request("GET", "http://api.weatherapi.com/v1/current.json?key=9d965cf9c7af4c8aabb132022201807&q=" + lat + "," + lon)
    return json.loads(array.data.decode('utf-8'))
