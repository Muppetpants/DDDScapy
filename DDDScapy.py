from scapy.all import *
 
recipients_mac_adress= 'ff:ff:ff:ff:ff:ff'
your_mac_adress= 'de:ad:be:ef:ca:fe'  #adjust as required
ssid = 'MuppetPants' #adjust as required
channel = chr(6)  #adjust as required
interface = 'wlan0mon'  #adjust as required
 
frame= RadioTap()\
      /Dot11(type=0, subtype=4, addr1=recipients_mac_adress, addr2=your_mac_adress, addr3=recipients_mac_adress)\
      /Dot11ProbeReq()\
      /Dot11Elt(ID='SSID', info=ssid)\
      /Dot11Elt(ID='Rates', info='\x82\x84\x8b\x96\x0c\x12\x18')\
      /Dot11Elt(ID='ESRates', info='\x30\x48\x60\x6c')\
      /Dot11Elt(ID='DSset', info=channel)\
      /Dot11Elt(ID='Vendor',info=b'\x00\x50\xf2\x99'
      b'' #Add payload from encryptThings.sh between the quotes
      )

frame.show()
print("\nHexdump of frame:")
hexdump(frame)
#wrpcap("DDDScapy.pcap",frame) #Uncomment to create/test pcap
sendp(frame, iface=interface, inter=5.00, loop=1) #adjust interval as required
