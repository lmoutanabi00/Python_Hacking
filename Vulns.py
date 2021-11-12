import PortScanner

target_ip = input('[+] Enter Your Target : ')
port_num = input('[+] Enter Range Of Port To Scan : ')
vul_file = input('[+] Enter Path File With Vulnerable Software : ')
print('\n')

target = PortScanner.PortScanner(target_ip, port_num)
target.scan()


with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(' !! Vulnerable Banner ' + banner + 'In Port ' + str(target.open_ports(count)))
        count += 1
