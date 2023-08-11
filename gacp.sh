#!/bin/bash

#Checks If file name is provided as argument
if [ $# -eq 1 ]; then
    file="$1"

    #Checks if file exits
    if [ -e "$file" ]; then
        git add $file
        echo -e "File '$file' added\n\n"
    else
        git add .
        echo -e "File(s) added\n\n"
    fi


    if [ -e "$file" ]; then
        git commit -m "Update '$file'"
        echo -e "\n"
        echo -e "File '$file' committed\n\n"

        git status

        git push
        echo -e "\n"
        echo -e "File already pushed\n\n"
        exit 0
    else
        echo -e "File '$file' does not exist\n\n"
        exit 1
    fi
else
    git add .
    git commit -m "Update files"
    echo -e "\n"
    echo -e "Files committed\n\n"
    git commit
    git push
fi
