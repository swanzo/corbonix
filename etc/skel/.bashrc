# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions

# tty1 successful login starts X
if [[ -z "$DISPLAY" ]] && [[ $(tty) = /dev/tty1 ]]; then
	startx
	logout
fi
