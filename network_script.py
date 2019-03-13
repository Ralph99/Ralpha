from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.google.coom",80))
s.send("GET / index.html HTTP/1.0\n\n")
data = s.recv(10000)
close