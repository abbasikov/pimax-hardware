import time
class TemperatureSensor:
    delayInSeconds = 4
    def __init__(self):
        print('TemperatureSensor constructed')

    def startPinging(self):
        while (True):
            time.sleep(self.delayInSeconds)
            print('TemperatureSensor pinging')
            print('')

