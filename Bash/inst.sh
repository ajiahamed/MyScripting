#!/usr/bin/env bash
#main script
scpath=~/Git/gitlab/OSscript/SH
. $scpath/up.sh

up_banner_01

update

echo " "

echo -e $magenta
read -n1 -s -r -p "Press any key to continue..."
echo -e $eoc
clear

sysinfo

read -p "The Process compleated..!" -t 5

clear
