import socket
from datetime import datetime

socket.setdefaulttimeout(1)

target = input("Enter target IP and hostname: ")


try:

    target_ip = socket.gethostbyname(target)

    print("-" * 50)

    print(f"Scanning Target: {target_ip}")

    print(f"Time Started: {datetime.now()}")

    print("-" * 50)


    for port in range(1, 1025):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
         result = scanner.connect_ex((target_ip, port))

        if result == 0:
           print(f"Port {port} is OPEN")
        

except KeyboardInterrupt:

    print("\nScan stopped by user.")    

except socket.gaierror:

    print("Hostname cannot be resolved.")

except socket.error as error:

    print(f"Network error: {error}")
