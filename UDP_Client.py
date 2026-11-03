
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

temp = input("Enter Temperature: ")
s.sendto(temp.encode(), ('localhost', 1235))

s.close()
