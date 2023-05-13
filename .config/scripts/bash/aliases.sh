# for nmcli wifi
# give name of wifi and its status
alias wifi-status="nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -c 5- | cut -c 1-20"
alias wifi-status-all="nmcli -t -f active,ssid dev wifi | cut -c 5- | cut -c 1-20"
# list all networks scanned 
alias wifi-scan="nmcli dev wifi rescan"
alias list-wifi="nmcli dev wifi list"

alias wifi-list="nmcli -t -f active,ssid dev wifi | cut -c 5-"
alias wifi-connect="nmcli dev wifi --ask connect"

alias connect-wifi="~/.config/scripts/wifi.sh"

alias qtile-map="cat ~/.config/qtile/config.py | grep Key"
alias tmux-map="cat ~/.config/tmux/tmux.conf | grep bind-key"
alias nvim-map='cat ~/.config/nvim/lua/mappings.lua | grep map'
alias mappings="~/.config/scripts/bash/cat-mappings.sh"

alias vim="nvim"
alias svim="sudo nvim"


# directory changing
alias ..="cd ../"
alias ...="cd ../../"
alias ....="cd ../../../"

# make and cd into directory
function mkcd() {
    mkdir -p -- "$1" &&
    cd -P -- "$1"
}

