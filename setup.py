import requests
import threading
import json
from sensors.temperature.TemperatureSensor import *
from sensors.smoke.SmokeSensor import *
from sensors.airpressure.AirPressure import  *
from sensors.humidity.HumiditySensor import *


tempSensor = TemperatureSensor()
smokeSensor = SmokeSensor()
airpressureSensor = AirPressureSensor()
humiditySensor = HumiditySensor()

configServerUrl = "https://pimax-hardware-config.herokuapp.com/config"
myResponse = requests.get(configServerUrl)
print(myResponse.text)
json_data = json.loads(myResponse.text)
print(json_data['config']['sensors'])
print('done')


if __name__ == "__main__":
    # creating threads
    tempThread = threading.Thread(target=tempSensor.startPinging)
    smokeThread = threading.Thread(target=smokeSensor.startPinging)
    airpressureThread = threading.Thread(target=airpressureSensor.startPinging)
    humidityThread = threading.Thread(target=humiditySensor.startPinging)

    # starting all threads
    tempThread.start()
    smokeThread.start()
    airpressureThread.start()
    humidityThread.start()

    # wait until thread 1 is completely executed
    #t1.join()

    # both threads completely executed
    print("Done!")


