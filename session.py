import socket

host = "google.com"
port = 80

C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    C.connect((host, port))
    print("conectado")
except Exception as e:
    print("Nao conectado: ", e)
    C.close
    exit()

C.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = C.recv(4096)

if response:
    print (response.decode(errors="ignore"))
else:
    print ("sem resposta")

C.close