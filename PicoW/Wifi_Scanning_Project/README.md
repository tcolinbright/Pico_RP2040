# Wifi Scanning Project
### Author:
#### Colin B.

<br><br/>

## Description:

### This directory includes the files I am using to build a wifi scanner using MicroPython, PicoW, and Pimironi Pico Display Pack 2.0.

## Requirements:
1. Raspberry Pi Pico W (with M headers for Display Pack)
1. Pimironi Micropython .UF2
1. Pimironi Pico Display Pack 2.0
1. Power supply - 5v (USB Battery Bank)
1. Thonny IDE

## Goal of Project:
To create a portable wifi scanner that can not only display available networks, but filter a specific BSSID and provide a real time AP tracker.

### Phase 1:
- Main screen will display newtworks and basic information from each scan.
- User can store unique SSID and BSSID on board (limited memory).
- User can view stored SSID nad BSSID.
- "Logging" will be optional.
- User will be able to delete stored .txt/.csv files.
- Standardized RGB LED patterns to be noted in Documentation.

### Phase 2:
- User will be able to scroll through list of scanned networks.
- User will be be able to select network to track.
- Screen will have graph to indicate dbm strength reading over time.
- Screen will have graph indicating current dbm strength.
- Screen will display average dbm reading over time.

### Phase 3:
- User will be able to turn pico into AP.
- User will be able to access stored SSID and BSSID.
- User will be able to download .txt/.csv from Pico.
- User will be able to upload .txt/.csv to Pico.

## Status:

### Phase 1:
Current progress is slow. Currently I can log to a file on the pico, making it possible to "save" remembered SSID and BSSID. Handy for War Driving. I can also have the user select the desired network and scan for that BSSID. It works, but if the signal drops out, the "bar graph" will keep displaying the last input it did receive.
- Need to filter using the raw scan tgt-BSSID against the raw scan. Its comparing bytes to bytes instead of converting it to hex to check.
- Will port over code from Pico_Explorer Display to use.
- Working on .jpeg backgorunds

