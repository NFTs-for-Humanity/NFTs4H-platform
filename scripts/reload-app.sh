#!/bin/bash
cd ~/nfts4h-platform
source env/bin/activate
cd nfts4h/
screen -d -m python manage.py runserver 0.0.0.0:8800