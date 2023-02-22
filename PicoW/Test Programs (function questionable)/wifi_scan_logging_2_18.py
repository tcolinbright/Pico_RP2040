'''
##### Logging Requirements ####
To log you will need to already have saved on Pi Pico:
- unique_bssid.txt
- unique_ssid.txt
based on what you want to log.

Remember theres not much memory on the little Pico.
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


#def create_bssid_list(scan):
    ''' Format/convert and return list of BSSIDs'''
    bssid_list_full = []
    networks = scan
    for net in networks:
    
        bssid = str(binascii.hexlify(net[1], ":")) #changes bytes to hex
        bssid = bssid.replace("b'", "")
        bssid = bssid.replace("'","")
        bssid_list_full.append(bssid)
    
    total_aps = len(bssid_list_full)
    print(f'Discovered {total_aps} Access Points\n')
    return bssid_list_full

 
def create_ssid_list(scan):
    '''Formats SSIDs from scan results. Returns list of all SSIDs'''
    ssid_list_full = []
    networks = scan
    for net in networks:
        ssid = str(net[0].decode('utf-8')) # <--- Testing.decode
        if ssid == "":
            ssid = "Hidden"
        else:
            ssid = ssid
        ssid_list_full.append(ssid)
    
    return ssid_list_full


def log_unique(input_list, check_against_list, append_to_file):
    '''Compares input_list to check_against list. If not present it appends to append_to_file'''
    for item in input_list:
        if item in check_against_list:
            continue
        else:
            check_against_list.append(item) # Save to current list so it doesn't multi record
            append_to_file(item, append_to_file, "\n")

def top_networks(show_top, scan, list_item_number, sort_desc):
    '''Sorts networks by list_item_number reading and returns the top n amount of them
    show_top = number of item to return like top 5
    scan = the nic.scan() output
    list_item_number = positional number in list. 
        0: SSID
        1: BSSID (bytes in raw output)
        2: Channel
        3: Decible
        4: Security (FLAWED)
        5: Hidden 1 = True | 2 = False
    sort_desc = sort in reverse order True/False'''
    
    def sort_by(e):
        return e[list_item_number]
    
    networks = scan
    networks.sort(key=sort_by, reverse=sort_desc) 
    networks = networks[0:show_top]
    return networks


def formatting(scan_output):
    '''Formats output to display in terminal'''
    for net in scan_output:
        
        ssid = str(net[0].decode('utf-8'))
        channel = net[2]
        dbm = net[3]
        #security = str(net[4]) #Outputs are inaccurate
        
        if ssid == "":
            ssid = "Hidden"
        else:
           ssid = ssid
        
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8')) #changes hex to normal numbers
        bssid = bssid.upper()
    
       
        print(f'SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Dbm: {dbm}\n\n-------------------\n')


def end_scan_line(scan_int):
    '''Ends line with printed *'s and sets interval between scans'''
    print("\n*********\n")
    time.sleep(scan_int)


def read_file_into_memory(input_file, delim):
    '''Reads file into a list splitting on delim. Returns list'''
    my_file = open(input_file, "r") # this is the file to read
    data = my_file.read() # reading the file
    new_list = data.split(delim) # split items in file by delim
    my_file.close() # close the file to prevent corruption
    return new_list


def append_to_file(item_to_append, to_file, delim):
    '''Takes item_to_append and appends it to_file, splitting on delim'''
    item_to_append = str(item_to_append)
    _txt = open(to_file, 'at')
    _txt.write(f'{item_to_append}{delim}')
    _txt.close()


def get_file_size(in_file): #NeedFix: return sizes as value strings
    '''Prints file size to terminal, returns file size value in KB and MB'''
    stats = os.stat(in_file)
    size_kbytes = round((stats[6] / 1024), 2)
    size_mbytes = size_kbytes / 1024
    print(f'{in_file} size:\n{size_kbytes} KB   |   {size_mbytes} MB\n')
    KB, MB = size_kbytes, size_mbytes
    return KB, MB


def blink_onboard_led_constant(num_blinks):
    '''Blinks led num_blinks amount of times at 100hz'''
    for i in range(num_blinks):
        led.on()
        time.sleep(.1)
        led.off()
        time.sleep(.1)


# Start Here #
blink_onboard_led_constant(5) #Flash to aknowledge boot

'''This can be uncommented for logging BSSIDs. Currently needs to have 'unique_bssid.txt' already saved to pico.'''
#unique_bssid = read_file_into_memory('unique_bssid.txt', "\n") 
#previously_collected_bssid = len(unique_bssid) - 1
#print(f'Imported {previously_collected_bssid} previously recorded BSSID')

'''Read in input_file.txt to a list. Return number of items imported'''
unique_ssid = read_file_into_memory('unique_ssid.txt', "\n")  
previously_collected_ssids = len(unique_ssid) - 1 # -1 accounts for \n character

'''Output to display File Size + Number of imported items + title to distinguish results'''
get_file_size('unique_ssid.txt')
print(f'Imported {previously_collected_ssids} previously recorded SSID')
print(f'\n\n*****    Scan Results    *****\n\n')


while True:
    '''Scans network, returns top results based on dbm, outputs to terminal, and logs
        if logging = True, any new SSIDs not found in imported list.
        LED blinks after each succesful scan+logging cycle to indicate operation.
        For 2 sec after LED blinks, the pico sleeps. Good time to unplug.'''
    scan = nic.scan() # Scan for broadcast
    total_networks_found(scan) # Display number of stations picked up
    networks = top_networks(n, scan, 3, True) # Get top n amount of networks based on dbm
    formatting(networks)
    if logging == True:
        #bssid_list = create_bssid_list(scan)
        #log_unique(bssid_list, unique_bssid, 'unique_bssid.txt')
        ssid_list = create_ssid_list(scan)
        log_unique(ssid_list, unique_ssid, 'unique_ssid.txt')
    else:
        pass
    
    blink_onboard_led_constant(1)
    end_scan_line(2)
    



