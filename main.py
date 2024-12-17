import socket
import yaml
import threading
import time
from src.ultra_sound_driver import UltraSoundDriver
from src.uart_scale_driver import UartScaleDriver
from src.udp_service_driver import UdpServiceDriver


ultra_sound_driver_api = UltraSoundDriver()
uart_scale_driver_api = UartScaleDriver()
udp_service_driver_api = UdpServiceDriver()

real_weight_data = 0
weight_flag = 0
weight_value = 0
ultra_sound_distance = 0

def ultra_sound_thread():
    global ultra_sound_distance
    ultra_sound_driver_api.enablePWM()

    while True:
        temp_ultra_sound_distance = ultra_sound_driver_api.getUltraDistance()
        if(temp_ultra_sound_distance is None):
            pass
        else:
            ultra_sound_distance = temp_ultra_sound_distance
            ## print("[Debug] temp_ultra_sound_distance is {} ".format(temp_ultra_sound_distance))

def scale_thread():
    global weight_flag, weight_value
    get_set_zero_cali_value = uart_scale_driver_api.set_to_zero_and_peel()
    print("get_set_zero_cali_value is {}".format(get_set_zero_cali_value))
    while True:
        temp_weight_flag, temp_weight_value = uart_scale_driver_api.get_weight_value()
        weight_flag = temp_weight_flag
        weight_value = temp_weight_value
        ## print("[Debug] scale thread: weight_flag is {}, weight_value is {}".format(temp_weight_flag, temp_weight_value))

def udp_service_thread():
    global real_weight_data, weight_flag, weight_value, ultra_sound_distance
    scale_message = None
    ultra_sound_message = None
    udp_service_driver_api.set_udp_service_net_info("config/udp_config.yaml")
    udp_service_driver_api.init_udp_service_basic_config()
    print(f"[Info] udp service is waitint for client ip")

    while True:
        ## udp_service_driver_api.get_udp_client_net_info()
        
        if(weight_flag == 0):
             real_weight_data = weight_value
        else:
            real_weight_data = weight_value * (-1)
    
        scale_message = "scale_message: " + str(real_weight_data)
        ultra_sound_message = "ultra_sound_message: " + str(ultra_sound_distance)

        udp_service_driver_api.send_udp_service_message(scale_message)
        udp_service_driver_api.send_udp_service_message(ultra_sound_message)
        
        time.sleep(0.05)
        
def udp_service_listen_thread():
    while True:
        udp_service_driver_api.get_udp_client_net_info()

def main(args=None):
    print("Start TASK")
    ultra_sound_thread_impl = threading.Thread(target=ultra_sound_thread)
    scale_thread_impl = threading.Thread(target=scale_thread)
    udp_service_thread_impl = threading.Thread(target=udp_service_thread)
    udp_service_listen_thread_impl = threading.Thread(target=udp_service_listen_thread)

    ultra_sound_thread_impl.start()
    scale_thread_impl.start()
    udp_service_thread_impl.start()
    udp_service_listen_thread_impl.start()

    while True:
        ## print("Idle...\r\n")
        time.sleep(1)

if __name__ == '__main__':
    main()
