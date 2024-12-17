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

def ultra_sound_thread():
    while True:
        ## print(f"ultra sound thread is running!")
        time.sleep(1)   

def scale_thread():
    get_set_zero_cali_value = uart_scale_driver_api.set_to_zero_and_peel()
    print("get_set_zero_cali_value is {}".format(get_set_zero_cali_value))
    while True:
        weight_flag, weight_value = uart_scale_driver_api.get_weight_value()
        print("[Debug] scale thread: weight_flag is {}, weight_value is {}".format(weight_flag, weight_value))
        time.sleep(0.1)

def udp_service_thread():
    udp_service_driver_api.set_udp_service_net_info("config/udp_config.yaml")
    udp_service_driver_api.init_udp_service_basic_config()
    print(f"[Info] udp service is waitint for client ip")
    udp_service_driver_api.get_udp_client_net_info()
    print(f"[Info] next!")

    while True:
        udp_service_driver_api.get_udp_client_net_info()
        
        udp_service_driver_api.send_udp_service_message()

        print(f"udp service thread is running!")
        
        time.sleep(0.2)

def main(args=None):
    print("Start TASK")
    ultra_sound_thread_impl = threading.Thread(target=ultra_sound_thread)
    scale_thread_impl = threading.Thread(target=scale_thread)
    udp_service_thread_impl = threading.Thread(target=udp_service_thread)

    ultra_sound_thread_impl.start()
    scale_thread_impl.start()
    udp_service_thread_impl.start()


    while True:
        ## print("Idle...\r\n")
        time.sleep(1)

if __name__ == '__main__':
    main()
