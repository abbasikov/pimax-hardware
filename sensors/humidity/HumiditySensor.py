import time
class HumiditySensor:
    serviceURL = ''
    pushDataToServer = 1
    pushIntervalInSeconds = 2

    def __init__(self, host, jsonObject):
        #self.pushIntervalInSeconds = jsonObject['pushIntervalInSeconds']
        #self.pushDataToServer = jsonObject['pushDataToServer']
        self.serviceURL = host+jsonObject['uri']
        print('HumiditySensor constructed ')

    def pushDataToServer(self):
        while (True):
            time.sleep(self.pushIntervalInSeconds)
            print('HumiditySensor pushDataToServer')
            print('')