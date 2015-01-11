#!/bin/bash

TS=$(date +"%d.%m.%y-%H:%M")
cp wikigraph.dot graphs/wikigraph.$TS.dot
cp wikigraph.png graphs/wikigraph.$TS.png
