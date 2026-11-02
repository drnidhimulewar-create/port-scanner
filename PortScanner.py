import socket
from datetime import datetime

target = input("Enter target IP and hostname: ")

target_ip = socket.gethostbyname(target)

print("-" * 50)

print(f"Scanning Target: {target_ip}")
print(f"Time Started: {datetime.now()}")

print("-" * 50)

try:

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
           print(f"Port {port} is OPEN")
        s.close

except KeyboardInterrupt:

    print("\nScan stopped by user.")    

except socket.gaierror:

    print("Hostname cannot be resolved.")

except socket.error:

    print("Server not responding.")
