#!/bin/bash

if [[ -e ".dhx.customized" ]]; then
    exit
fi

if [[ -e "$DHX_USER_INIT" ]]; then
    if [[ -d "$DHX_USER_INIT" ]]; then
        init_files="$(ls $DHX_USER_INIT)"
        if [[ -n "$init_files" ]]; then
            for script in "$init_files"; do
                $DHX_USER_INIT/$script || exit $?
            done
        fi
    else
        ./$DHX_USER_INIT || exit $?
    fi
    rm -rf "$DHX_USER_INIT"
fi

touch .dhx.customized
