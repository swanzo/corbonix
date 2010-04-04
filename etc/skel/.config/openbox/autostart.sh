# Run the system-wide support stuff
#. $GLOBALAUTOSTART

# Programs to launch at startup
# =============================

# Force openoffice.org to use GTK theme
# enable this if you install openoffice
#export OOO_FORCE_DESKTOP=gnome

# Start volume control system tray applet
gmixer -d &

# Set desktop wallpaper
nitrogen --restore &

# Launch network manager applet
(sleep 4s && nm-applet) &

# Launch clipboard manager
#(sleep 1s && parcellite) &

# Uncomment to enable system updates at boot
#(sleep 180s && gpk-update-icon) &

# Launch Conky
conky -q &

# Launch panel
tint2 &
