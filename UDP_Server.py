
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1235))

print("Waiting for temperature...")

while True:
    data, addr = s.recvfrom(1024)
    print("Temperature:", data.decode())
