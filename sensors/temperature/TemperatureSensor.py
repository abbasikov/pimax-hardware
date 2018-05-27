import time
import random
import requests
class TemperatureSensor:
    serviceURL = ''
    pushDataToServer = 1
    pushIntervalInSeconds = 2

    def __init__(self, host, jsonObject):
        #self.pushIntervalInSeconds = jsonObject['pushIntervalInSeconds']
        #self.pushDataToServer = jsonObject['pushDataToServer']
        self.serviceURL = host+jsonObject['uri']
        print('TemperatureSensor constructed ')

    def pushDataToServer(self):
        while (True):
            try:
                print('TemperatureSensor pushDataToServer')
                time.sleep(self.pushIntervalInSeconds)
                tempInC = random.randint(10, 50)
                response = requests.post(self.serviceURL, data={'tempInC': tempInC})
            except Exception as inst:
                print('Error:')
                print(inst)