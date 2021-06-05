#!/bin/bash

# Reads a word from stdin.
function read_word() {
    read -p 'Enter word: ' word
    echo "${word}"
}

# Searches a stored word in application.
function find_word() {
    result=$(./show_words.py | grep -i ${1})

    if [[ -z ${result} ]]; then
        echo "Didn't found entries matching '${1}'."
    else
        word_count=$(echo "${result}" | wc -l)
        echo "Found ${word_count} entries matching '${1}':"
        # Warning: has to be enclosed in double quotes elsewere it removes any '\n' chars.
        echo "${result}"
    fi
}

# If a word was given as an argument just find that word.
if [[ -n ${1} ]]; then
    find_word ${1}
else
    while [[ true ]]; do
        word=$(read_word)

        if [[ -n $word ]]; then
            find_word ${word}
        else
            echo "Done."
            exit 0
        fi
    done
fi
