import requests
import threading
import json
from sensors.temperature.TemperatureSensor import *
from sensors.smoke.SmokeSensor import *
from sensors.airpressure.AirPressureSensor import  *
from sensors.humidity.HumiditySensor import *
configServerUrl = "https://pimax-hardware-config.herokuapp.com/config"

config = requests.get(configServerUrl)
print(config.text)
json_data = json.loads(config.text)
print(json_data)
print('config done')

tempSensor = TemperatureSensor(json_data['config']['host'],json_data['config']['sensors']['temperature'])
smokeSensor = SmokeSensor(json_data['config']['host'],json_data['config']['sensors']['smoke'])
airpressureSensor = AirPressureSensor(json_data['config']['host'],json_data['config']['sensors']['airPressure'])
humiditySensor = HumiditySensor(json_data['config']['host'],json_data['config']['sensors']['humidity'])


if __name__ == "__main__":
    # creating threads
    tempThread = threading.Thread(target=tempSensor.pushDataToServer)
    smokeThread = threading.Thread(target=smokeSensor.pushDataToServer)
    airpressureThread = threading.Thread(target=airpressureSensor.pushDataToServer)
    humidityThread = threading.Thread(target=humiditySensor.pushDataToServer)

    # starting all threads
    tempThread.start()
    smokeThread.start()
    airpressureThread.start()
    humidityThread.start()

    # wait until thread 1 is completely executed
    #t1.join()

    # both threads completely executed
    print("Sensors started")


