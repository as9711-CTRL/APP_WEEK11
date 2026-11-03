
import socket

s = socket.socket()
s.connect(('localhost', 1234))

reg = input("Enter Register Number: ")
s.send(reg.encode())

print("Result:", s.recv(1024).decode())

s.close()
