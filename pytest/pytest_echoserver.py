#!/usr/bin/python3
import socket
import sys
import os
import datetime
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    s.bind((host_name, 9000))
    s.listen(5)
    port_num = sys.argv[1]
    print "Listening on port number", port_num
    i = 1
    while True:
        clientsocket, address = s.accept()
        print "Server: Connection from ", address
        while True:
            #s = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            message = clientsocket.recv(1024)
            file_name = "echo_response_" + str(i) + ".txt" 
            test_file = open(file_name, "wb")
            #print(ts)
            #print(message)
            #print(address)
            out = str(message) + '\n' + str(address)
            test_file.write(bytes(out))
            i = i + 1
            test_file.close()
            if message == "":
                break
            if message == "EXIT" or "__EXIT__":
                sys.exit(0)
        clientsocket.close()

