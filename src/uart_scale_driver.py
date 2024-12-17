from periphery import Serial
import time
import numpy as np

class UartScaleDriver:
    def __init__(self):
        self.serial = Serial("/dev/ttyS3", 9600, 8, "none", 1, True, False)

    def send_data(self, data):
        self.serial.write(data)

    def receive_data(self):
        data_buff = self.serial.read(16, 0.5)
        return data_buff

    def measure_the_AD_value_directly(self): 
        data = bytes([0xA1, 0x00, 0xA0, 0xA2, 0xA3])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data

    def get_weight_value(self):
        data = bytes([0xA3, 0x00, 0xA2, 0xA4, 0xA5])
        self.send_data(data)
        receive_data = self.receive_data()
        weight_flag = receive_data[3]
        weight_value = (receive_data[4]*65536) + (receive_data[5]*256) + receive_data[6]
        return weight_flag, weight_value
    
    def set_zero_calibration(self):
        data = bytes([0xAA, 0x00, 0xA9, 0xAB, 0xA8])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data

    def set_to_zero_and_peel(self):
        data = bytes([0xAB, 0x00, 0xAA, 0xAC, 0xAD])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data

    def cancel_set_to_zero_and_peel(self):
        data = bytes([0xAC, 0x00, 0xAB, 0xAD, 0xAA])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data

    def set_weight_calibration(self, data_high, data_low):
        xor_data = np.uint8(0xAD ^ 0x00 ^ data_high ^ data_low)
        data = bytes([0xAD, 0x00, data_high, data_low, xor_data])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data

    def set_factory_data_reset(self):
        data = bytes([0x51, 0x00, 0x50, 0x52, 0x53])
        self.send_data(data)
        receive_data = self.receive_data()
        return receive_data
        



