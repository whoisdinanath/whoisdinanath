# connect wifi using nmcli and ask for ssid and password as input

read -p "SSID: " SSID
read -sp "Password: " PASSWORD
echo ""


sudo nmcli dev wifi connect $SSID password $PASSWORD
