import rain
import humidity_temperature as dht

rain_count = rain.count()
temp = dht.temp()
humidity = dht.humidity()

print(f"rain_count = {rain_count} temperature {temp} humidity = {humidity}")
