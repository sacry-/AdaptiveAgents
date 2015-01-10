#!/bin/bash

TS=$(date +"%d.%m.%y-%H:%M")
cp wikigraph.dot graphs/wikigraph.dot.$TS
cp wikigraph.png graphs/wikigraph.png.$TS
