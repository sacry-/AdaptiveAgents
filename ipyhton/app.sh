#!/bin/bash

if [ -z "$1" ]; then
    bash /media/swaneet/88C899ADC89999D0/xubuntu/elasticsearch-1.3.4/bin/elasticsearch > /dev/null &
    ipython notebook --matplotlib='inline' --notebook-dir='/media/swaneet/88C899ADC89999D0/Users/Swaneet/github/AdaptiveAgents' --no-browser > /dev/null &
    exit 0
fi

pkill -f "elasticsearch"
pkill -9 -f "AdaptiveAgents"
