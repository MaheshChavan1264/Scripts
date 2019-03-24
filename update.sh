#!/bin/bash
echo "Select 1 or 2"
read ch
if [ $ch  -eq 1 ]
then
    sudo apt update
    sudo apt dist-upgrade -yy
if [ $ch -eq 2 ]
then

    sudo apt-get autoremove -yy
    sudo apt-get auoclean
    fi
fi
echo "---------------------------"
echo "- Update complete -"
echo "---------------------------"

exit