#!/bin/bash

echo 
echo 'Enter word:'
read word

echo 
echo 'Search results:'
# Flag -i ignores case
./show_words.py | grep -i "$word"
