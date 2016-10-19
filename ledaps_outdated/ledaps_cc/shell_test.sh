#!/bin/bash
echo -n "Enter Source Directory:"
read srcdir
echo $srcdir

read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
echo "good"
fi
