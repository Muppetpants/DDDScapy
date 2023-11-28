# DDDScapy

Hacky AF, working on a complete python build. 

This attempts to include encrypted payloads within a probe request information element. Looks weird, but who's looking at probes? (We are!) 

1. Ensure adapter is in monitor mode and camped on desired channel.
2. Use Encrypt script to build payload and transmit 
3. Extract payload (IEEE 802.11 Wireless Management>Tag: Vendor Specific, Right click, copy, as Hex Stream) 
4. Paste entire hex stream into decrypt script
5. Profit

Will eventually consolidate everything into a single python tool, look at stuffing Beacons, and maybe parse through encrypted text files, line by line. Maybe.
