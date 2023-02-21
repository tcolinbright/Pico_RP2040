''' outputs a backwards bar graph. Think of star as the AP and the dashes are distance.
need to change logic on what to do when the bssid isnt located in scan
known bug: will just keep displaying last dbm in list. need to limit list '''

import binascii
import network
import time
import os


def scan_for(bssid_in, in_scan):
    for net in in_scan:
        ssid = str(net[0].decode('utf-8'))
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8'))
        bssid = bssid.upper()
        dbm = net[3]
        if bssid == bssid_in:
            dbm_recording.append(dbm)
        else:
            pass


def trim_list(list_name, limit):
    if len(list_name) > limit:
        list_name.pop(0)
        return list_name


def get_avg(in_list):
    average = sum(in_list)/len(in_list)
    return average


def simple_barchart(in_list):
    dbm = in_list[-1]
    pos_dbm = abs(dbm)
    bar_length = pos_dbm * 2
    bar = f'  {dbm} dbm |' + ("-"  * bar_length) + "*"
    print(bar)


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


def scan_cycle(tgt_bssid):
    while True:
        scan = nic.scan()
        networks = top_networks(n, scan, 3, True)
        trim_list(dbm_recording, 1)
        scan_for(tgt_bssid, networks)
        simple_barchart(dbm_recording)
        time.sleep(1)
        #print(dbm_recording)


def formatting(scan_output):
    '''Formats output to display in terminal'''
    item_number = 0
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
    
        
        print(f'{item_number}: SSID: {ssid}\nBSSID: {bssid} | CH: {channel}  | Dbm: {dbm}\n-------------------')
        item_number += 1



#####################################################
nic = network.WLAN(network.STA_IF)
nic.active(True)
n = 5

''' Scan for Access Points and return top n amount.'''
scan = nic.scan()
networks = top_networks(n, scan, 3, True) 
formatting(networks)

dbm_recording = [0,]


user_selection = int(input("Select which station to scan: "))
tgt_net = networks[user_selection]

tgt_bssid = str(binascii.hexlify(tgt_net[1], ":").decode('utf-8')) #changes hex to normal numbers
tgt_bssid = tgt_bssid.upper()


scan_cycle(tgt_bssid)



