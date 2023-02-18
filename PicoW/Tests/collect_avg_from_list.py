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


def create_dbm_list(scan):
    '''Formats dbms from scan results. Returns list of all dbms'''
    dbm_list_full = []
    networks = scan
    for net in networks:
        dbm = str(net[3])
        dbm_list_full.append(dbm)
    
    return dbm_list_full


def log_unique(input_list, check_against_list, append_to_file):
    '''Compares input_list to check_against list. If not present it appends to append_to_file'''
    for item in input_list:
        if item in check_against_list:
            continue
        else:
            check_against_list.append(item) # Save to current list so it doesn't multi record
            append_to_file(item, append_to_file, "\n")