#Created By: Milad Khoshdel
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkhoshdel

import sys
import requests
import socket
import json
import nmap

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
Target_IP = socket.gethostbyname(sys.argv[1])

print("\n\n[ Main information ]")
print("Server: " + str(req.headers['Server']))
print("Content-Type: " + str(req.headers['Content-Type']))
if 'Set-Cookie' in req.headers:
    print("Set-Cookie: " + str(req.headers['Set-Cookie']))
print("Server IP: " + sys.argv[1] + " is " + Target_IP)

print("\n[ Extra information from external API ]")
req_two = requests.get("https://ipinfo.io/" + Target_IP + "/json")
resp_ = json.loads(req_two.text)
print("IP: " + resp_["ip"])
print("HostName: " + resp_["hostname"])
print("city: " + resp_["city"])
print("Region: " + resp_["region"])
print("country: " + resp_["country"])
print("Location: " + resp_["loc"])
print("Owner: " + resp_["org"])
print("TimeZone: " + resp_["timezone"])

print("\n[ Port Scan ]")
target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]

scan_it = nmap.PortScanner()

print("Scanning", target, "for ports 21, 22, 80, 139, 443, 8080 ...")

PortScan = scan_it.scan(Target_IP, '80')
print("Host", Target_IP, "is" , PortScan["scan"][Target_IP]["status"]["state"])

for port in ports:
    PortScan = scan_it.scan(Target_IP, str(port))
    print("Port", port, ":" , PortScan["scan"][Target_IP]["tcp"][port]["state"])
