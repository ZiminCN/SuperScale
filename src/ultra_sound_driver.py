from periphery import GPIO
from periphery import PWM
import time

class UltraSoundDriver:
    def __init__(self):
        self.Trigger_Chip = 11      ## PWM10_1
        self.Trigger_Channel = 0    ## PWM10_1
        self.Echo_Pin = 54          ## GPIO1_C7_d

        self.StartTime = 0
        self.EndTime = 0
        self.TimeDelta = 0
        self.Distance = 0

        self.Trigger_PWM = PWM(self.Trigger_Chip, self.Trigger_Channel)
        self.Echo_GPIO = GPIO(self.Echo_Pin, "in")

        ## 100 hz, high 10us, low 9.9ms
        self.Trigger_PWM.frequency = 100
        self.Trigger_PWM.duty_cycle = 0.001
        self.Trigger_PWM.polarity = "normal"
        ## self.Trigger_PWM.enable()

    def enablePWM(self):
        self.Trigger_PWM.enable()

    def getUltraDistance(self):
        ## try read ultra sound

        ## 1. Enter low level echo sign
        if(self.Echo_GPIO.read() is False):

        ## 2. if Enter high level echo sign, start record start time
            if(self.Echo_GPIO.read() is True):
                self.StartTime = time.time()

        ## 3. if Enter low level echo sign, start record end time
                while self.Echo_GPIO.read() is True:
                    # idle
                    pass
                self.EndTime = time.time()

        ## 4. calculate ultra-sound total time and get distance
                self.TimeDelta = self.EndTime - self.StartTime
                self.Distance = (self.TimeDelta * 34300) / 2

        ## 5. return distance
                print("Distance is {}".format(self.Distance))
                return self.Distance
            else:
                pass
        else:
            pass


