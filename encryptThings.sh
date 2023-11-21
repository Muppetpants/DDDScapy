#!/bin/bash
#encryptThings.sh
clear
read -p "Message to be encrypt:" message
encrypted=$(echo $message | openssl enc -e -aes-256-cbc -a -salt 2>/dev/null)
hex=$(echo $encrypted | xxd -p | tr -d '\n' | sed 's/\(..\)/\\x\1/g')
clear
echo "Paste the following into the DDDScapy.py script"
echo $hex
