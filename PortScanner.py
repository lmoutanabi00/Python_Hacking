import socket
from IPy import IP


class PortScanner:
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def banner(self):
        print('[+] P0rt Scan3R v1.0')
        print('[+] Made With Code ')
        print('''

   ██████╗░██████╗░██████╗░██████╗░░█████╗░
   ██╔══██╗╚════██╗╚════██╗██╔══██╗██╔══██╗
   ██████╔╝░█████╔╝░█████╔╝██║░░██║███████║          
   ██╔══██╗░╚═══██╗░╚═══██╗██║░░██║██╔══██║            
   ██║░░██║██████╔╝██████╔╝██████╔╝██║░░██║
   ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═ 
    Author: r33da
    IG    : r33.mikhail 
_______________________________________________ ''')

    def scan(self):
        for port in range(1, 500):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                pass
        except:
            pass

    banner()
