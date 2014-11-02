#!/bin/bash

# elasticsearch: "http://localhost:9200/_plugin/kopf"
# ipython: "http://localhost:8888/"

if [ -z "$1" ]; then
    bash $WINR/xubuntu/elasticsearch-1.3.4/bin/elasticsearch -Des.path.data=$WINR/xubuntu/elasticsearch-1.3.4/data > /dev/null &
    ipython notebook --matplotlib='inline' --notebook-dir=$WIN/github/AdaptiveAgents --no-browser > /dev/null &
    exit 0
fi

pkill -f "elasticsearch"
pkill -9 -f "AdaptiveAgents"
