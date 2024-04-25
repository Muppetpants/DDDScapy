#!/bin/bash
#decryptThings.sh
clear
read -p "Message to be decrypted:" message

payload=$(echo $message | cut -c 13-) 

output=$(echo -ne  $payload | xxd -r -p | openssl enc -d -aes-256-cbc -a -salt 2>/dev/null)
clear
echo "Decrypted Message:"
echo $output