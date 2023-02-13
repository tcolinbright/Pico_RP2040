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

#def unique(input_list):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in input_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)


def get_unique_bssid(input_list):
    unique_bssid = []

    for bssid in input_list:
        if bssid in unique_bssid:
            continue
        else:
            unique_bssid.append(bssid)
    return unique_bssid


def log_bssid(uniq_bssid):
    bssid_file = open('unique_bssid.txt', 'at')
    bssid_file.write(uniq_bssid)
    bssid_file.close()



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
bssid_list = create_bssid_list(scan)
#print(bssid_list)
uniq_bssid = get_unique_bssid(bssid_list)
print(uniq_bssid)
log_bssid(uniq_bssid)

end_scan_line(2)
