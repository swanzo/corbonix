#!/bin/bash
exe=`dmenu_path | dmenu -fn -*-terminus-*-*-*-*-*-*-*-*-*-*-*-* -nb '#A7C3DD' -nf '#224058' -sb '#224058' -sf '#A7C3DD'` && eval "exec $exe"
