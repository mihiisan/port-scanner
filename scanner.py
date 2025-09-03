import socket
import time
import pyfiglet

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)


target = input('What you want to scan?: ')
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # don’t hang forever
        s.connect((target_ip, port))
        s.close()
        return True
    except:
        return False

start = time.time()

for port in range(5):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')