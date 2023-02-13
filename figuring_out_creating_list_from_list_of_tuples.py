import network
import binascii
import time
nic = network.WLAN(network.STA_IF)
nic.active(True)
 
n = 4 #number of networks to show (based on strongest singnals in this case)
scan_time = 2 #number of seconds between scans

def total_networks_found(scan):
    networks_found = len(scan)
    print(f'Total Networks Found: {networks_found}\n')
    return networks_found

def create_bssid_list(scan):
    bssid_list_full = []
    networks = scan
    for net in networks:
    
        bssid = str(binascii.hexlify(net[1], ":")) #changes hex to normal numbers
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")
        bssid_list_full.append(bssid)
    
    total_aps = len(bssid_list_full)
    print(f'Discovered {total_aps} Access Points')
    return bssid_list_full



def top_networks(show_top, scan):
    
    def sort_by_dbm(e):
        return e[1]
    
    networks = scan
    networks.sort(key=sort_by_dbm, reverse=True)
    networks = networks[0:show_top]
    print(networks)
    return networks

def end_scan_line(scan_int):
    print("\n*********\n")
    time.sleep(scan_int)



scan = nic.scan()
#top_networks(10, scan)
#total_networks_found(scan)
bssid_uniq = create_bssid_list(scan)
print(bssid_uniq)
end_scan_line(2)
