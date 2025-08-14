import time
import board
import adafruit_dht

# Initialize DHT device, with data pin connected to GPIO4
dht_device = adafruit_dht.DHT11(board.D4)  # Change to DHT11 if using that sensor

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temp: {temperature_c:.1f}°C    Humidity: {humidity:.1f}%")
    except RuntimeError as error:
        # Read errors happen from time to time
        print(error.args[0])
    time.sleep(2)

