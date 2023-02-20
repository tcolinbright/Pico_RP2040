import binascii
import network


nic = network.WLAN(network.STA_IF)
nic.active(True)

scan = nic.scan()

for net in scan:
    ssid = str(net[0].decode('utf-8'))
    bssid = str(binascii.hexlify(net[1], ":").decode('utf-8'))
    bssid = bssid.upper()
    if ssid == "":
        ssid = "Hidden"
        print(f'SSID: {ssid}\n')
        print(f'BSSID: {bssid}\n')
    else:
        print(f'SSID: {ssid}\n')
        print(f'BSSID: {bssid}\n')