#!/bin/zsh

# cat nvim config file and show the keybindings
echo "\n\n"
echo "+---------------------+"
echo "   nvim keybindings   "
echo "+---------------------+"
echo "\n\n"
cat ~/.config/nvim/lua/mappings.lua | grep "map(\""

# cat tmux conf file and show the keybindings
echo "\n\n"
echo "+---------------------+"
echo "   tmux keybindings   "
echo "+---------------------+"
echo "\n\n"
cat ~/.config/tmux/tmux.conf | grep bind-key

# cat qtile config and show the keybindings
echo "\n\n"
echo "+---------------------+"
echo "   qtile keybindings   "
echo "+---------------------+"
echo "\n\n"
cat ~/.config/qtile/config.py | grep "Key("