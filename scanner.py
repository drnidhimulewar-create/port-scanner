import socket

def scan(target, start, end):
    ip = socket.gethostbyname(target)
    open_ports = []
    for port in range(start,end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip,port)) == 0:
                open_ports.append(port)
    return ip, open_ports
           