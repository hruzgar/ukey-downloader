#!/bin/bash
# ukeydl uninstallation script
# Maintainer: Ferit Yigit BALABAN
# https://github.com/hruzgar/ukey-downloader

set -e
steps=3
installdir=/usr/local/bin
desktopfiledir=$HOME/.local/share/applications

echo "This script removes ukeydl and related files from your system"
echo "If you've changed anything in install script you should intervene now and change in this file as well"
echo

echo "(1/$steps) Removing folder $installdir/ukey-downloader and contents"
sudo rm -rf $installdir/ukey-downloader

echo "(2/$steps) Removing ukeydl from $installdir"
sudo rm $installdir/ukeydl

echo "(3/$steps) Removing ukeydl.desktop from $desktopfiledir"
sudo rm "$desktopfiledir"/ukeydl.desktop

echo
echo "Uninstallation is complete"