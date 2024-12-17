import socket
import numpy as np
import yaml

class UdpServiceDriver:
    def __init__(self):
        self.udp_service_ip = "192.168.50.1"
        self.udp_service_port = "5050"
        self.udp_client_addr = None
        self.service_socket = None
        self.is_connect_with_client = False

    def set_udp_service_net_info(self, udp_config_yaml):
        with open(udp_config_yaml, 'r') as file:
            udp_config_info = yaml.safe_load(file)
        self.udp_service_ip = udp_config_info["udp_service"]["ip"]
        self.udp_service_port = udp_config_info["udp_service"]["port"]
        print("udp_service_ip is {}, udp_service_port is {} ".format(self.udp_service_ip, self.udp_service_port))

    def init_udp_service_basic_config(self):
        self.service_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.service_socket.bind((self.udp_service_ip, self.udp_service_port))
        print("Init udp service basic config\r\n")

    def get_udp_client_net_info(self):
        if(self.service_socket is None):
            return

        data, addr = self.service_socket.recvfrom(1024)

        if(data.decode() != "0xDEADCODE"):
            print(f"Received message: {data.decode()} from udp client {addr}")
            return
        else:
            self.udp_client_addr = addr
            self.is_connect_with_client = True
            print(f"Received message: {data.decode()} from udp client {addr}")

    def send_udp_service_message(self, message):
        if(self.service_socket is None):
            return

        if(self.is_connect_with_client is False):
            return

        tx_message = str(message)
        self.service_socket.sendto(tx_message.encode(), self.udp_client_addr)
        

