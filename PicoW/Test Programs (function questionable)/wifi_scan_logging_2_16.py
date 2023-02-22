'''
blink Led
optional logging added
##### Compare with other versions and clean up repo  ########

'''


import network
import binascii
import time
import os
from machine import Pin

nic = network.WLAN(network.STA_IF)
nic.active(True)
led = Pin("LED", Pin.OUT)
n = 4 #number of networks to show (based on strongest singnals in this case)
scan_time = 2 #number of seconds between scans
logging = True

   
def total_networks_found(scan):
    ''' Returns the length of the list of tuples equating to number of discovered networks'''
    number_of_networks_found = len(scan)
    print(f'Total Networks Found: {number_of_networks_found}\n')
    return number_of_networks_found


def create_bssid_list(scan):
    ''' Format/convert and return list of BSSIDs'''
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


#def get_unique_bssid(input_list):
#     for bssid in input_list:
#         if bssid in unique_bssid:
#             continue
#         else:
#             unique_bssid.append(bssid)
#             bssid_csv = open(r'unique_bssid.csv', 'at')
#             bssid_csv.write(f'{bssid},')
#             bssid_csv.close()
    

def create_ssid_list(scan):
    '''Formats SSIDs from scan results. Returns list of all SSIDs'''
    ssid_list_full = []
    networks = scan
    for net in networks:
        ssid = str(net[0])
        if ssid == "b''":
            ssid = "Hidden"
        else:
            ssid = ssid.replace("b'", "")
            ssid = ssid.replace("'","")
        ssid_list_full.append(ssid)
    
    return ssid_list_full


def get_unique_ssid(input_list):
    '''Checks input list against stored list. Appends to list if not present.'''
    for ssid in input_list:
        if ssid in unique_ssid:
            continue
        else:
            unique_ssid.append(ssid)
            # ssid_txt = open(r'unique_ssid.txt', 'at')
            # ssid_txt.write(f'{ssid}\n')
            # ssid_txt.close()
            append_to_file(ssid, "unique_ssid.txt", "\n") #Testing this function to condense lines of code


def top_networks(show_top, scan):
    '''Sorts networks by dbm reading and returns the top n amount of them'''
    
    def sort_by_dbm(e):
        return e[3]
    
    networks = scan
    networks.sort(key=sort_by_dbm, reverse=True) 
    networks = networks[0:show_top]
    return networks

def formatting(scan_output):
    '''Formats output to display in terminal'''
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
       
        print(f'SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Dbm: {dbm}\n\n-------------------\n')


def end_scan_line(scan_int):
    '''Ends line with printed *'s and sets interval between scans'''
    print("\n*********\n")
    time.sleep(scan_int)


#def read_into_list(in_list, append_list): #Was redundant. Add to utility class
#     '''Take items from in_list and append to append_list. Returns new combined list.'''
#     input_list = in_list
#     output_list = append_list
#     for item in input_list:
#         append_list.append(item)
#     return output_list


def read_file_into_memory(input_file, delim):
    '''Reads file into a list splitting on delim. Returns list'''
    my_file = open(input_file, "r") # this is the file to read
    data = my_file.read() # reading the file
    new_list = data.split(delim) # split items in file by delim
    my_file.close() # close the file to prevent corruption
    return new_list


def append_to_file(item_to_append, to_file, delim):
    '''Takes item_to_append and appends it to_file, splitting on delim'''
    _txt = open(to_file, 'at')
    _txt.write(f'{item_to_append}{delim}')
    _txt.close()


def get_file_size(in_file): #NeedFix: return sizes as value strings
    '''Prints file size to terminal'''
    stats = os.stat(in_file)
    size_kbytes = round((stats[6] / 1024), 2)
    size_mbytes = size_kbytes / 1024
    to_display = print(f'{in_file} size:\n{size_kbytes} KB   |   {size_mbytes} MB\n')
    return to_display


def blink_onboard_led_constant(num_blinks):
    '''Blinks led num_blinks amount of times at 100hz'''
    for i in range(num_blinks):
        led.on()
        time.sleep(.1)
        led.off()
        time.sleep(.1)

# Start Here #
blink_onboard_led_constant(5)

#unique_bssid = read_file_into_memory('unique_bssid.txt', "\n") 
#previously_collected_bssid = len(unique_bssid) - 1
#print(f'Imported {previously_collected_bssid} previously recorded BSSID')

unique_ssid = read_file_into_memory('unique_ssid.txt', "\n")  
previously_collected_ssids = len(unique_ssid) - 1 # -1 accounts for \n character

get_file_size('unique_ssid.txt')
print(f'Imported {previously_collected_ssids} previously recorded SSID')
print(f'\n\n*****    Scan Results    *****\n\n')

while True:
    scan = nic.scan()
    total_networks_found(scan)
    networks = top_networks(n, scan)
    formatting(networks)
    if logging == True:
        #bssid_list = create_bssid_list(scan)
        #get_unique_bssid(bssid_list)
        ssid_list = create_ssid_list(scan)
        get_unique_ssid(ssid_list)
    else:
        pass
    
    end_scan_line(2)
    blink_onboard_led_constant(1)



