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
    print(f'Discovered {total_aps} Access Points\n')
    return bssid_list_full


# def get_unique_bssid(input_list):
#     #unique_bssid = []
# 
#     for bssid in input_list:
#         if bssid in unique_bssid:
#             continue
#         else:
#             unique_bssid.append(bssid)
#     return unique_bssid


def get_unique_bssid(input_list):
    for bssid in input_list:
        if bssid in unique_bssid:
            continue
        else:
            unique_bssid.append(bssid)
            bssid_txt = open(r'unique_bssid.txt', 'at')
            bssid_txt.write(f'{bssid}\n')
            bssid_txt.close()
    return unique_bssid


# #def log_bssid(uniq_bssid):
#     bssid_list = open(r'unique_bssid.txt', 'at')
#     for bssid in uniq_bssid:
#         bssid_list.write(f'{bssid}\n')
#     bssid_list.close()


def top_networks(show_top, scan):
    '''Sorts networks by dbm reading and returns the top n amount of them'''
    
    def sort_by_dbm(e):
        return e[3]
    
    networks = scan
    networks.sort(key=sort_by_dbm, reverse=True)
    networks = networks[0:show_top]
    return networks

def formatting(scan_output):
    for net in scan_output:
        
        ssid = str(net[0])
        channel = net[2]
        dbm = net[3]
        #security = str(net[4])
        
        if ssid == "b''":
            ssid = "Hidden"
        else:
            ssid = ssid.replace("b'", "")
            ssid = ssid.replace("'","")
        
        bssid = str(binascii.hexlify(net[1], ":")) #changes hex to normal numbers
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")

 #Security codes are outputting different codes from documentation
#         if security == '0':
#             security = "Open"
#         elif security == '1':
#             security = "WEP"
#         elif security == '2':
#             security = "WPA-PSK"
#         elif security == '3':
#             security = "WPA2-PSK"
#         elif security == '4':
#             security = "WPA/WPA-PSK"
       
        print(f'SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Dbm: {dbm}\n\n-------------------\n')
        #print(f'---------------------\n\nSSID: {ssid}\nBSSID: {bssid}\nCH: {channel}\nDb: {dbm}\nSecurity: {security}\n')
        #print(f'Security: {security}')
   
def end_scan_line(scan_int):
    print("\n*********\n")
    time.sleep(scan_int)

unique_bssid = []

while True:
    scan = nic.scan()
    total_networks_found(scan)
    bssid_list = create_bssid_list(scan)
    get_unique_bssid(bssid_list)
    #print(unique_bssid)
    networks = top_networks(n, scan)
    formatting(networks)
    #log_bssid(uniq_bssid)
    end_scan_line(2)
