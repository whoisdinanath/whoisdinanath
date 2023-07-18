# ~/.zshrc

<<<<<<< HEAD
#for scilab
alias xcos="IBGL_ALWAYS_SOFTWARE=1 MESA_GL_VERSION_OVERRIDE=3.0 scilab"

export STARSHIP_CONFIG=~/.config/starship/starship.toml
export FLYCTL_INSTALL="/home/bibek/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
export PATH="/home/bibek/.local/bin:$PATH"
export PATH="/home/bibek/bin:$PATH"
export PATH=/usr/local/texlive/2023/bin/x86_64-linux:$PATH
=======
export STARSHIP_CONFIG=~/.config/starship/starship.toml
  export FLYCTL_INSTALL="/home/bibek/.fly"
  export PATH="$FLYCTL_INSTALL/bin:$PATH"
export PATH="/home/bibek/.local/bin:$PATH"
export PATH="/home/bibek/bin:$PATH"
>>>>>>> 6631689f46084f35a0c17c22b9f59b6a029895f6
# tab case insensitive
if [[ -n $commands[compaudit] ]]; then
  compaudit | xargs chmod g-w
fi
<<<<<<< HEAD
. $HOME/.asdf/asdf.sh
=======

>>>>>>> 6631689f46084f35a0c17c22b9f59b6a029895f6
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




