#!/bin/bash
curl -I $1 2> err.txt | grep "Location:" | cut -d ' ' -f 2
rm err.txt