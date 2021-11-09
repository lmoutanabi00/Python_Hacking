import socket
from IPy import IP


def banner():
    print('[+] P0rt Scan3R v1.0')
    print('[+] Made With Code ')
    print('''

   ██████╗░██████╗░██████╗░██████╗░░█████╗░
   ██╔══██╗╚════██╗╚════██╗██╔══██╗██╔══██╗
   ██████╔╝░█████╔╝░█████╔╝██║░░██║███████║          
   ██╔══██╗░╚═══██╗░╚═══██╗██║░░██║██╔══██║            
   ██║░░██║██████╔╝██████╔╝██████╔╝██║░░██║
   ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═ 

    🇦​​​​​🇺​​​​​🇹​​​​​🇭​​​​​🇴​​​​​🇷​​​​​ : r33da
    IG    : r33.mikhail
    
    ''')
  
#Scan The ip in range(1-100)
def Scan(target):
  converted_ip = check_ip(targets)
  print('\n'+' [0] Target Scanning... ' + str(target))
  for port in range(1,100):
    Scan_port(converted_ip, port)

# Convert domain names to IP
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

# Get The Banner Of Each Port        
def get_banner(s):
  return s.recv(1024)

# Scan The Specific Ip And Port With The Banner (ssh,FTP..)
def Scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        try:
          ban= get_banner(sock)
          print('[+] Open Port ' +str(port)+ ':' + str(ban.decode().strip('\n')))
        except:
          print('[+] Open Port ' +str(port))
    except:
        pass

banner()

# Check If The User Enter Multiple Target 
if __name__ == "__main__": # If__name function it's for Hid This Part Of Code To Not get Run If We Import This Portscanner
  targets = input('Enter Your Target : ')
  if ',' in targets:
    for ip_idd in targets.split(','):
        Scan(ip_idd.strip(' '))
  else:
    Scan(targets)

# 06/11/2021 
