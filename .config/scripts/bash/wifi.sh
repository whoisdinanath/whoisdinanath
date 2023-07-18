#!/bin/zsh
# connect wifi using nmcli and ask for ssid and password as input

read "SSID: " SSID
read "Password: " PASSWORD
echo ""


sudo nmcli dev wifi connect $SSID password $PASSWORD
