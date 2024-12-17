import socket

udp_ip = "192.168.19.155"
udp_port = 5050

service_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

service_socket.bind((udp_ip, udp_port))

print("UDP service is listening...")

data, addr = service_socket.recvfrom(1024)
print(f"Received message: {data.decode()} from {addr}")

while True:
    response_message = "Message received!"
    service_socket.sendto(response_message.encode(), addr)
