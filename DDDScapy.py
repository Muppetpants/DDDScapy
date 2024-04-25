from scapy.all import *

# Vars
recipients_mac_adress= 'ff:ff:ff:ff:ff:ff'
your_mac_adress= 'de:ad:be:ef:ca:fe'  #adjust as required
ssid = 'MuppetPants' #adjust as required
channel = chr(6)  #adjust as required
interface = 'wlan0mon'  #adjust as required
# Using readlines()
file1 = open('file.txt', 'r')
Lines = file1.readlines()
count = 0

# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    new_line = bytes(line.strip(), 'utf-8')
    frame= RadioTap()\
      /Dot11(type=0, subtype=4, addr1=recipients_mac_adress, addr2=your_mac_adress, addr3=recipients_mac_adress)\
      /Dot11ProbeReq()\
      /Dot11Elt(ID='SSID', info=ssid)\
      /Dot11Elt(ID='Rates', info='\x82\x84\x8b\x96\x0c\x12\x18')\
      /Dot11Elt(ID='ESRates', info='\x30\x48\x60\x6c')\
      /Dot11Elt(ID='DSset', info=channel)\
      /Dot11Elt(ID='Vendor',info=b'\x00\x50\xf2\x99'+ new_line)
    wrpcap("DDDScapy" + str(count) + ".pcap",frame) #Uncomment to create/test pcap
    frame.show()
    print("\nHexdump of frame:")
    hexdump(frame)
    #sendp(frame, iface=interface, count=10, inter=1./10)) #adjust interval as required
