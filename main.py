import socket
import yaml
import threading
from src.ultra_sound_driver import UltraSoundDriver

ultra_sound_driver = UltraSoundDriver()

def main(args=None):
    print("Start TASK")
    ultra_sound_driver.enablePWM()
    while True:
        ultra_sound_driver.getUltraDistance()

if __name__ == '__main__':
    main()
