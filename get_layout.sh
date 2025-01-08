#!/bin/sh


found=`hyprctl devices | grep -Pzo 'Keyboard at .*\n(\t\t.*\n)+(\t\t\tmain: yes)' | grep --text "active keymap" | sed "s/.*active keymap: //g" | awk '{print tolower($0)}'`
found="${found:0:2}"

echo $found
