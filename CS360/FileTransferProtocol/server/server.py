#Server for transferring files across the internet
#Setup for localhost
import socket

HOST = '127.0.0.1'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #AF_INET is address family for IPv4
    #SOCK_STREAM is the socket type for TCP

    s.bind((HOST, PORT))
    s.listen()
  
    conn, addr = s.accept()
    #Block and wait for connection
    with conn:
        filename = conn.recv(1024).decode() #Get file name of file being sent by user
        with open(filename, 'wb') as f:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024) # Received the file's bytes and write them to a new file
                f.write(data)
                if not data:
                    break
            conn.shutdown(socket.SHUT_WR)