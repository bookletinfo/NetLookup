import socket

def convert_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0] if ip.replace('.', '').isdigit() else socket.gethostbyname(ip)
    except socket.herror:
        return "Hostname not found!"
    except socket.gaierror:
        return "Invalid IP address!"

ip = input("Enter an IP address or domain name: ")
print("Result:", convert_ip(ip))
