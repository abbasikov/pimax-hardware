import time
class AirPressureSensor:
    delayInSeconds = 1
    def __init__(self):
        print('AirPressureSensor constructed')

    def startPinging(self):
        while (True):
            time.sleep(self.delayInSeconds)
            print('AirPressureSensor pinging')
            print('')