
import socket

s = socket.socket()
s.bind(('localhost', 1234))
s.listen(1)

print("Server waiting...")
c, addr = s.accept()

reg = c.recv(1024).decode()

results = {
    '101': 'Pass - 85%',
    '102': 'Pass - 90%',
    '103': 'Fail - 40%'
}

result = results.get(reg, "Student Not Found")
c.send(result.encode())

c.close()
s.close()
