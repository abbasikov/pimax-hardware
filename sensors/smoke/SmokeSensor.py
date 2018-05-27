import time
class SmokeSensor:
    delayInSeconds = 3
    def __init__(self):
        print('SmokeSensor constructed')

    def startPinging(self):
        while (True):
            time.sleep(self.delayInSeconds)
            print('SmokeSensor pinging')
            print('')