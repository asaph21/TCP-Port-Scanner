import socket
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import json
import ipaddress


start = time.time()

try:
    target = sys.argv[1]
    target = socket.gethostbyname(target)
    port_start = int(sys.argv[2])
    port_end = int(sys.argv[3])
except socket.gaierror:
    print("[-] Invalid host")
    sys.exit()
except IndexError:
    print("[-] Usage: python scanner.py <target> <port_start> <port_end>")
    sys.exit()

if port_start < 1:
    print("[-] Error")
    sys.exit()
if port_start > port_end:
    print("[-] Error")
    sys.exit()
if port_end > 65535:
    print("[-] Error")
    sys.exit()

open_ports = []

ip_obj = ipaddress.ip_address(target)

if ip_obj.is_private:
    ip_type = "Private"
elif ip_obj.is_loopback:
    ip_type = "Loopback"
elif ip_obj.is_multicast:
    ip_type = "Multicast"
elif ip_obj.is_reserved:
    ip_type = "Reserved"
else:
    ip_type = "Public"

def scan(port):
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(1)
    result = a.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = ("Unknown")

        try:
            a.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n") 
            ban_grab = a.recv(1024).decode(errors="ignore").strip()
        except:
            ban_grab = "No banner grabbing"
        if port == 443:
            ban_grab = "HTTPS - TLS handshake required"
        print(f"[+] Port {port} Open | {service} | {ban_grab}")

        open_ports.append({
            "port": port,
            "service": service,
            "banner": ban_grab
        })
    a.close()

print(f"\n[*] Scanning {target} | Type: {ip_type}\n")

with ThreadPoolExecutor(max_workers=200) as executor:
    executor.map(scan, range(port_start, port_end + 1)) 

end = time.time()

with open("report.json", "w") as f:
    json.dump(open_ports, f, indent=4)

print(f"\n[*] Scan finished in {end - start:.2f} seconds.")
