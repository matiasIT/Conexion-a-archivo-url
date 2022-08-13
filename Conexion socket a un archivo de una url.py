import socket

"""
Programa que recive una url dada por el usuario con informacion a la que se conecta a travez del puerto 80 para obtener la data codificada, y
la decodifica antes de imprimirla en pantalla.
"""

print("Put END to finish the program")
while True:
    count = 0
    url = input("Enter your URL: ")
    if url == "END":
        break
    try:
        host = url.split("/")[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = "GET" + url + "HTTP/1.0\r\n\r\n"
        cmd =  cmd.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            print(data.decode())
        mysock.close()
    except:
        print("Enter a valid HTTP//: format URL")
