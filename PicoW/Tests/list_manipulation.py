''' Sorts on known bssid and if found collects the strength reading for the scan
Plan is to do math with the list to gather averages and to produce a graph and strength meter'''

import binascii
import network
import time

nic = network.WLAN(network.STA_IF)
nic.active(True)




def scan_for(bssid_in):
    for net in scan:
        ssid = str(net[0].decode('utf-8'))
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8'))
        bssid = bssid.upper()
        dbm = net[3]
        
        if bssid == bssid_in:
            dbm_recording.append(dbm)
            #print(f'SSID: {ssid}\n')
            #print(f'BSSID: {bssid}\n')
            #print(f'Dbm {dbm}\n')
            #print("\n*************************\n\n")
        else:
            #print(f'Could not locate: {bssid}\n')
            #dbm_recording.append(0)
            pass


def trim_list(list_name, limit):
    if len(list_name) > limit:
        list_name.pop(0)
        return list_name


def get_avg(in_list):
    average = sum(in_list)/len(in_list)
    return average


def simple_barchart(in_list):
    for dbm in in_list:
        pos_dbm = abs(dbm)
        bar_length = pos_dbm
        bar = f'  {dbm} dbm |' + ("-"  * bar_length)
        print(bar)


def other_barchart(in_list):
    dbm = in_list[-1]
    pos_dbm = abs(dbm)
    bar_length = pos_dbm
    bar = f'  {dbm} dbm |' + ("-"  * bar_length) + "*"
    print(bar)


dbm_recording = []


while True:
    scan = nic.scan()
    trim_list(dbm_recording, 3)
    

    #dbm_avg = get_avg(dbm_recording)
    #scans_used = len(dbm_recording)
    #print(f'Avg: {dbm_avg} dbm')
    #print(f'Avg of {scans_used} previous scans.\n')
    #simple_barchart(dbm_recording)
    scan_for("00:71:C2:6F:5A:80")
    other_barchart(dbm_recording)
    time.sleep(2)

