
#Clienttcp
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))

msg = s.recv(1024)
print(msg.decode("utf-8"))

s.close()
