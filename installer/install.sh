#!/bin/bash
# ukeydl installation script
# Maintainer: Ferit Yigit BALABAN
# https://github.com/hruzgar/ukey-downloader

set -e
steps="6"
installdir=/usr/local/bin
desktopfiledir="$HOME/.local/share/applications/"
scriptdir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

cd "$scriptdir"
echo "This script installs ukeydl and related files to $installdir"
echo "You can change installdir variable to install to a different location"
echo "But this will break the ukeydl.desktop and ukeydl files, you should edit them first"
echo

echo "(1/$steps) Creating folder $installdir/ukey-downloader if not created already"
sudo mkdir --parents $installdir/ukey-downloader

echo "(2/$steps) Copying run.py to $installdir"
sudo cp ../run.py $installdir/ukey-downloader/.

echo "(3/$steps) Copying ukeydl (runs the python script) to $installdir"
sudo cp ukeydl $installdir/.

echo "(4/$steps) Setting permissions for ukeydl"
sudo chmod +x $installdir/ukeydl
sudo chmod 755 $installdir/ukeydl

echo "(5/$steps) Creating folder $desktopfiledir if not created already"
sudo mkdir --parents "$desktopfiledir"

echo "(6/$steps) Copying ukeydl.desktop (allows integration with built-in and third-party launchers) to $desktopfiledir"
sudo cp ukeydl.desktop "$desktopfiledir/."

echo
echo "Installation is complete."