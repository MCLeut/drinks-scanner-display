#!/bin/bash
xinput set-prop "eGalax Inc. USB TouchController" "Evdev Axes Swap" "1"
xinput set-prop "eGalax Inc. USB TouchController" "Coordinate Transformation Matrix" 1.3 0 -0.15 0 1.3 -0.15 0 0 1

while [ 1 ];
do
    cd /home/pi/drinks-scanner-display && ENV=PI python game.py
done