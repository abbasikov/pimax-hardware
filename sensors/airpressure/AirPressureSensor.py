import time
class AirPressureSensor:
    serviceURL = ''
    pushDataToServer = 1
    pushIntervalInSeconds = 2

    def __init__(self, host, jsonObject):
        #self.pushIntervalInSeconds = jsonObject['pushIntervalInSeconds']
        #self.pushDataToServer = jsonObject['pushDataToServer']
        self.serviceURL = host+jsonObject['uri']
        print('AirPressueSensor constructed ')

    def pushDataToServer(self):
        while (True):
            time.sleep(self.pushIntervalInSeconds)
            print('AirPressueSensor pushDataToServer')
            print('')