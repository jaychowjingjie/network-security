#!/usr/bin/python3
import socket
import sys
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port_num = sys.argv[1]
    message = sys.argv[2]
    # print(host_name)
    # print(message)
    s.connect((host_name, 9000))
    s.sendall(message.encode('utf-8'))
    s.close()
