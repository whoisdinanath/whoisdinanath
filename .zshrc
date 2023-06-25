# ~/.zshrc

export STARSHIP_CONFIG=~/.config/starship/starship.toml
  export FLYCTL_INSTALL="/home/bibek/.fly"
  export PATH="$FLYCTL_INSTALL/bin:$PATH"
export PATH="/home/bibek/.local/bin:$PATH"
export PATH="/home/bibek/bin:$PATH"
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

#if [[ -z "$TMUX" ]] && [[ "$SSH_CONNECTION" == "" ]]; then
#  tmux attach-session -t local_tmux || tmux new-session -s local_tmux
#fi
# if [[ -z "$TMUX" ]] && [[ "$SSH_CONNECTION" == "" ]]; then
#   tmux attach-session -t local_tmux || tmux new-session -s local_tmux
# fi

# aliases directory : ~/.config/scripts/bash/aliases.sh
source ~/.config/scripts/bash/aliases.sh

eval "$(starship init zsh)"




