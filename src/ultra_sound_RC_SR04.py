from periphery import GPIO
from periphery import PWM
import time

## use PWM port as trigger pin
Trigger_Chip = 11 ## PWM10_1
Trigger_Channel = 0 ## PWM10_1
Echo_Pin = 54 ## GPIO1_C7_d

Trigger_PWM = PWM(Trigger_Chip, Trigger_Channel)
Echo_GPIO = GPIO(Echo_Pin, "in")

## 10 hz, high 10us, low 99.9ms
Trigger_PWM.frequency = 100
Trigger_PWM.duty_cycle = 0.001
Trigger_PWM.polarity = "normal"
Trigger_PWM.enable()
StartTime = 0
EndTime = 0
TimeDelta = 0
Distance = 0

def getUltraDistance():   
    ## try read ultra sound
    
    ## 1. Enter low level echo sign
    if(Echo_GPIO.read() is False):

    ## 2. if Enter high level echo sign, start record start time
        if(Echo_GPIO.read() is True):
            StartTime = time.time()

    ## 3. if Enter low level echo sign, start record end time
            while Echo_GPIO.read() is True:
                # idle 
                pass
            EndTime = time.time()

    ## 4. calculate ultra-sound total time and get distance
            TimeDelta = EndTime - StartTime
            Distance = (TimeDelta * 34300) / 2

    ## 5. return distance
            print("Distance is {}".format(Distance))
            return Distance
        else:
            pass
    else:
        pass

if __name__ == '__main__':
    Trigger_PWM.enable()
    while True:
        ## StartTime = time.time()
        ## print("StartTime is {}".format(StartTime))
        ## time.sleep(1)
        ## EndTime = time.time()
        ## print("EndTime is {}".format(EndTime))
        ## TimeDelta = EndTime - StartTime
        ## Distance = (TimeDelta * 34300) / 2
        ## Distance = round(Distance/100, 2)
        ## print("Distance is {} cm".format(Distance))
        ## time.sleep(1)
        ## print("Distance is {:.2f} cm".format(getUltraDistance()))  
        getUltraDistance()

