#!/bin/bash

if [[ -e ".jdhe.customized" ]]; then
    exit
fi

if [[ -e "$JDHE_USER_INIT" ]]; then
    if [[ -d "$JDHE_USER_INIT" ]]; then
        for script in "$(ls $JDHE_USER_INIT)"; do
            $JDHE_USER_INIT/$script
        done
    else
        ./$JDHE_USER_INIT
    fi
    rm -rf "$JDHE_USER_INIT"
fi

touch .jdhe.customized
