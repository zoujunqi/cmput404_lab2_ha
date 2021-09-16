#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    
    #create socket, bind, and set to listening mode
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(2)

        while True:
            #connect proxy_start
            conn, addr = s.accept()
            p = Process(target=handle_echo,args=(addr,conn))
            p.daemon = True
            p.start()
            print("Started process", p)
        
#echo connections back to client
def handle_echo(addr,conn):
    pritn("Connected by", addr)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()

if __name__ == "__main__":
    main()