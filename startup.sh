#! /bin/bash
source ~/.profile
workon audiobot
python audiobot.py > /dev/null 2>&1 &
