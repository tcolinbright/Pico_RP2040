''' Sorts on known bssid and if found collects the strength reading for the scan
Plan is to do math with the list to gather averages and to produce a graph and strength meter'''

import binascii
import network
import time

nic = network.WLAN(network.STA_IF)
nic.active(True)

scan = nic.scan()


def scan_for(bssid_in):
    for net in scan:
        ssid = str(net[0].decode('utf-8'))
        bssid = str(binascii.hexlify(net[1], ":").decode('utf-8'))
        bssid = bssid.upper()
        dbm = net[3]
        
        if bssid == bssid_in:
            dbm_recording.append(dbm)
            print(f'SSID: {ssid}\n')
            print(f'BSSID: {bssid}\n')
            print(f'Dbm {dbm}\n')
            print("\n*************************\n\n")
        else:
            pass


def trim_list(list_name, limit):
    if len(list_name) > limit:
        list_name.pop(0)
        return list_name

dbm_recording = []


while True:
    trim_list(dbm_recording, 10)
    print(dbm_recording)
    scan_for("00:71:C2:6F:5A:80")
    time.sleep(2)

