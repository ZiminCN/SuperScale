from periphery import Serial
import time

serial = Serial("/dev/ttyS3", 9600, 8, "none", 1, True, False)

while True:

    serial.write(bytes([0xA3, 0x00, 0xA2, 0xA4, 0xA5]))

    buf = serial.read(128, 0.5)

    neg_flag = buf[3]

    weight = (buf[4]*65536) + (buf[5]*256) + buf[6]

    print("neg_flag: {}, weight: {}".format(neg_flag, weight))

    time.sleep(1/10)

serial.close()
