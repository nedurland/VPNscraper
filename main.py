import socket
import ipaddress

# Driver code
def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # connect() for UDP doesn't send packets
    s.connect(('10.0.0.0', 0))
    print(s.getsockname()[0])
    
    found_vpn_pool = False
    
    vpn_name = ["VCEPOL21", "VCEPOL22", "VCEPOL23", "VCEPOL24", "VCEPOL41", "VCEPOL42", "VCEPOL43", "VCEPOL44", "VCEPOL45", "VCEPOL50", "VCEPOL51", "VCEPOL54", "VCEPOL55", "VCETTN21", "VCETTN22", "VCETTN41", "VCETTN42",
                "VCETTN43", "VCETTN44", "VCETTN45", "VCETTN50", "VCETTN51", "VCECHR21", "VCECHR22", "VCECHR41", "VCECHR42", "VCECHR44", "VCECHR45", "VCECHR50", "VCECHR51", "VCEBEL21", "VCEBEL21", "VCEBEL22", "VCEBEL22"]
    vpn_pool = ["5.250.96.0/21", "5.250.104.0/21", "5.250.84.0/23", "5.250.86.0/23", "5.250.160.0/21", "5.250.168.0/21", "5.250.0.0/21", "5.249.0.0/21", "5.249.16.0/21", "5.249.128.0/21", "5.249.136.0/21", "5.249.192.0/22", "5.249.196.0/22", "5.250.112.0/21", "5.250.120.0/21", "5.250.176.0/21", "5.250.184.0/21",
                "5.250.16.0/21", "5.249.24.0/21", "5.249.32.0/21", "5.249.144.0/21", "5.249.152.0/21", "5.250.136.0/21", "5.250.152.0/21", "5.249.40.0/21", "5.249.56.0/21", "5.249.48.0/21", "5.249.64.0/21", "5.249.72.0/21", "5.249.80.0/21", "10.145.71.0/24", "10.169.118.0/24", "10.145.72.0/24", "10.169.119.0/24"]
    eit_nat_pool = ["10.156.16.0/21", "10.156.24.0/21", "10.156.4.0/23", "10.156.6.0/23", "10.129.16.0/21", "10.129.48.0/21", "10.129.80.0/21", "10.156.96.0/21", "10.156.104.0/21", "10.156.232.0/21", "10.156.240.0/21", "10.61.52.0/22", "10.61.60.0/22", "10.148.224.0/21", "10.148.232.0/21", "10.129.144.0/21",
                    "10.129.176.0/21", "10.129.208.0/21", "10.129.24.0/21", "10.129.56.0/21", "10.18.192.0/21", "10.18.200.0/21", "10.12.232.0/21", "10.12.240.0/21", "10.129.88.0/21", "10.129.216.0/21", "10.129.152.0/21", "10.129.184.0/21", "10.18.208.0/21", "10.18.216.0/21", "10.40.82.0/24", "10.40.4.0/24", "10.40.83.0/24", "10.40.5.0/24"]
    nmnet_nat_pool = ["10.253.96.0/21", "10.253.104.0/21", "10.253.68.0/23", "10.253.70.0/23", "10.254.160.0/21", "10.254.168.0/21", "10.251.64.0/21", "10.251.48.0/21", "10.251.56.0/21", "10.242.80.0/21", "10.242.88.0/21", "10.247.76.0/22", "10.247.80.0/22", "10.255.112.0/21", "10.255.120.0/21", "10.254.176.0/21", "10.254.184.0/21",
                      "10.249.104.0/21", "10.255.208.0/21", "10.255.216.0/21", "10.242.96.0/21", "10.242.104.0/21", "10.250.136.0/21", "10.250.152.0/21", "10.245.72.0/21", "10.245.80.0/21", "10.249.80.0/21", "10.249.200.0/21", "10.242.112.0/21", "10.242.120.0/21", "5.232.38.0/24", "5.232.126.0/24", "5.232.78.0/24", "5.232.127.0/24"]

    vpnInfo = socket.gethostname()
    hostname = s.getsockname()[0]
    IP = socket.gethostbyname(hostname)
    
    ## What is going to be returned
    vpn_pool_ip = IP
    eit_nat_pool_ip = ""
    nmnet_nat_pool_ip = ""
    
    #print ("\nThe IP address", IP, "was not found in a known VPN pool")
    for i in range(len(vpn_name)):
        # Is the IP address in the VPN pool?
        if ipaddress.ip_address(IP) in ipaddress.ip_network(vpn_pool[i]):
            # Set VPN pool found flag to True
            found_vpn_pool = True
            
            # Calculate the offset from first IP address in the pool
            offset = int(ipaddress.ip_address(IP)) - int(ipaddress.ip_network(vpn_pool[i])[0])

            print("\nThe IP address was found in VPN pool", i, "on", vpn_name[i], "at offset", offset)

            # Print the VPN server and pool info
            vpn_pool_ip = IP
            eit_nat_pool_ip = ipaddress.ip_address(int(ipaddress.ip_network(eit_nat_pool[i])[0]) + offset)
            nmnet_nat_pool_ip = ipaddress.ip_address(int(ipaddress.ip_network(nmnet_nat_pool[i])[0]) + offset)
            print("\nVPN pool IP address:", IP)
            print("EIT NAT pool IP address:", ipaddress.ip_address(int(ipaddress.ip_network(eit_nat_pool[i])[0]) + offset))
            print("NMNet NAT pool IP address:", ipaddress.ip_address(int(ipaddress.ip_network(nmnet_nat_pool[i])[0]) + offset))
            
            # No need to check the rest of the pools
            break
    return { 
      "found_vpn_pool": found_vpn_pool,
      "vpn_info": vpnInfo,
      "vpn_pool_ip": vpn_pool_ip,
      "eit_nat_pool_ip": eit_nat_pool_ip,
      "nmnet_nat_pool_ip": nmnet_nat_pool_ip
    }
