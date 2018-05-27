import time
class HumiditySensor:
    delayInSeconds = 2
    def __init__(self):
        print('HumiditySensor constructed')

    def startPinging(self):
        while (True):
            time.sleep(self.delayInSeconds)
            print('HumiditySensor pinging')
            print('')