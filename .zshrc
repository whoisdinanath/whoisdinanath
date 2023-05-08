# ~/.zshrc

export STARSHIP_CONFIG=~/.config/starship/starship.toml

export PATH="/home/bibek/.local/bin:$PATH"

# tab case insensitive
if [[ -n $commands[compaudit] ]]; then
  compaudit | xargs chmod g-w
fi

autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

# start tmux on login
if [[ -z "$TMUX" ]] && [[ "$SSH_CONNECTION" != "" ]]; then
  tmux attach-session -t ssh_tmux || tmux new-session -s ssh_tmux
fi

# start tmux on opening terminal

if [[ -z "$TMUX" ]] && [[ "$SSH_CONNECTION" == "" ]]; then
  tmux attach-session -t local_tmux || tmux new-session -s local_tmux
fi
# if [[ -z "$TMUX" ]] && [[ "$SSH_CONNECTION" == "" ]]; then
#   tmux attach-session -t local_tmux || tmux new-session -s local_tmux
# fi



# for nmcli wifi
alias wifi-status="nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -c 5-" 
alias wifi-list="nmcli -t -f active,ssid dev wifi | cut -c 5-"
alias wifi-connect="nmcli dev wifi --ask connect"

alias connect-wifi="~/.config/scripts/wifi.sh"

alias vim="nvim"
alias svim="sudo nvim"

eval "$(starship init zsh)"




