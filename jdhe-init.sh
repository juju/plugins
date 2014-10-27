#!/bin/bash

if [[ -e ".jdhe.customized" ]]; then
    exit
fi

if [[ -e "$JDHE_USER_INIT" ]]; then
    if [[ -d "$JDHE_USER_INIT" ]]; then
        init_files="$(ls $JDHE_USER_INIT)"
        if [[ -n "$init_files" ]]; then
            for script in "$init_files"; do
                $JDHE_USER_INIT/$script || exit $?
            done
        fi
    else
        ./$JDHE_USER_INIT || exit $?
    fi
    rm -rf "$JDHE_USER_INIT"
fi

touch .jdhe.customized
