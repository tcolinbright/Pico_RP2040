import network
import binascii
import time
nic = network.WLAN(network.STA_IF)
nic.active(True)
 
n = 4 #number of networks to show (based on strongest singnals in this case)
scan_time = 2 #number of seconds between scans



def sort_by_dbm(e):
    return e[3]

def top_networks():
    networks = nic.scan()
    networks.sort(key=sort_by_dbm, reverse=True)
    networks = networks[0:n]
    return networks

def formatting(scan_int, scan_output):
    for net in scan_output:
        
        ssid = str(net[0])
        channel = net[2]
        dbm = net[3]
        security = str(net[4])
        
        if ssid == "b''":
            ssid = "Hidden"
        else:
            ssid = ssid.replace("b'", "")
            ssid = ssid.replace("'","")
        
        bssid = str(binascii.hexlify(net[1], ":")) #changes hex to normal numbers
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")

        if security == '0':
            security = "Open"
        elif security == '1':
            security = "WEP"
        elif security == '2':
            security = "WPA-PSK"
        elif security == '3':
            security = "WPA2-PSK"
        elif security == '4':
            security = "WPA/WPA-PSK"
        
        print(f'SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Db: {dbm}  | Security: {security}\n\n-------------------\n')
        #print(f'---------------------\n\nSSID: {ssid}\nBSSID: {bssid}\nCH: {channel}\nDb: {dbm}\nSecurity: {security}\n')
        #print(f'Security: {security}')
    print("\n*********\n")
    time.sleep(scan_int)


while True:
    networks = top_networks()
    top_networks()
    formatting(2, networks)