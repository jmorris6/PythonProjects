import socket

HOST = '127.0.0.1'
PORT = 9999
fileName = input("Enter full file name: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(fileName.encode()) #Send the file name
    with open(fileName, 'rb') as f: #Read and send the file by its bytes
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)
    s.shutdown(socket.SHUT_WR)

