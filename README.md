# DDDScapy

Hacky AF, but it's working. 

Purpose: 
This script allows the user to "stuff" probe requests with arbitrary data.  
TX Usage: 
Edit file.txt and add the message to be stuffed. 
Edit DDDScapy.py, particularly the following fields: 
your_mac_adress (This field will spoof the MAC address in the transmitted frames)
ssid (The SSID that will be directly probed )
channel (transmit channel)
interface (wlan interface to transmit -- I've always set to wlan0mon via airmon-ng)

After edits, you can run the script with python3 DDDScapy.py to test the script and write the outputs to output. If satisfied with the pcaps, uncomment the final line "#sendp" and run the script again. 

RX Usage
Receivers should be tuned to the specific channel 
e.g. sudo airmon-ng start wlan0 6 

Receivers should write to output with whatever collection tool they're using 
e.g. sudo airodump-ng -c 6 -w DDD wlan0mon

In a packet analyzer, stuffed probes can be filtered and then viewed within the bottom field of each probe request
wlan.fc.type_subtype==4 && wlan.ssid contains "<target SSID>"
or
wlan.fc.type_subtype==4 && wlan.sa==<MAC ADDRESS>


Wireshark will display extra spaces within the message. To clean, copy the appropriate field as an ASCII stream and run through xxd -r -p 
