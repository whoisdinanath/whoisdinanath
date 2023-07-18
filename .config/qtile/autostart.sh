#!/usr/bin/env bash 

#festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
#conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with feh
feh --bg-fill $HOME/Wallpaper/png/b-009.png &

# get the battery percentage and time at startup
battery=$(acpi | awk '{print $4}' | tr -d ',')
# store this value in a file in /tmp so that it can be accessed by other scripts
echo $battery > /tmp/battery