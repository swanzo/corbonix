#!/bin/bash

# Begin

clear

# Splash

echo -e "\033[33m                                     _
                    _               (_)             
  ____   ____  __  / /_  ____  ____  _ __  __
 / ___\ / __ \/ _\/ _  \/ __ \/ __ \| |\ \/ /
/ /____/ /_/ / / / /_/ / /_/ / / / /| | )  (
\_____/_____/_/  \____/_____/_/ /_/ |_|/_/\_\ 
         \033[34m__,--,_\033[m9
 _____\033[31m,-\033[34m'_______\033[m\\\\\\\\\033[31m-,\033[m_____  The Fedora based operating
<____/\033[31m\\\\\\ \033[34m\_\033[33mo\033[34m__\033[33mO\033[34m_\033[m// \033[31m/\033[m\____> system that powers Astroid
  ( \033[34m|  \033[31m\\\\\\      \033[m(.)\033[31m/  \033[34m| \033[m)   Blue Heaven.
  / \033[34m|   \033[31m}}      {{   \033[34m| \033[m\ 
 / /\033[34m|   \033[31m||     \033[mk\033[31m||   \033[34m|\033[m\ \  Swanzo, the chief mechanic
{ ( \033[34m|   \033[31m||    \033[mlk\033[31m||\033[m\  \033[34m| \033[m) } maintains Corbonix with the
 \ \\\\\033[34m|   \033[31m||   \033[m/|\\\\\033[31m||\033[m\  \033[34m|\033[m/ /  utmost care.  Working along
  \_\\\\\\033[31m===\033[m{}\033[31m======\033[m{}\033[31m===\033[m/_/   side his aide; Mikey helps
  (_}\033[34m-,____________,-\033[m{_)   test Corbonix on various
  / |  | |      | |  | \   ships.
 (__/  | |      | |  \__)
       ( |      | )        Corbonix is known to work
       | |      | |        very well on ships
       |_|      |_|        containing the i686.
 \033[31m,---\033[33m_\033[31m'  |      |  '\033[33m_\033[31m---,
{_________)    (_________} \033[34mastroidblueheaven.blogspot.com\033[m
"


# Question

read -p "Ready to install corbonix (y/n) ? "


# Install

if [ "$REPLY" == "y" ]; then

clear

sudo aptitude install \
alsa-utils \
build-essential \
devscripts \
git-core \
xorg \
dwm-tools \
conky \
scrot \
screen \
mc \
htop \
vim-full \
texlive \
epdfview \
irssi \
bitlbee \
mozilla-mplayer \
mutt \
newsbeuter \
rtorrent \
ubuntu-restricted-extras \
ffmpeg \
moc \
imagemagick

clear

fi


# Reboot

read -p "Finished installing corbonix, reboot (y/n) ? "

if [ "$REPLY" == "y" ]; then

clear

sudo reboot

fi

