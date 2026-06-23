import socket
import time
import threading
import sys

usage = "python3 port_scan.py Target start_port end_port"

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()


try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

def scan_port(port):
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    conn = s.connect_ex((target,port))
    if(not conn):
        print("Port {} is OPEN".format(port))
    s.close()


threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(
        target=scan_port,
        args=(port,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
