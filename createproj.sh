#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo $0: 'Need project name'
    exit 1
fi
docker-compose run web django-admin startproject $1 \.

sudo chown -R $USER:$USER $1 manage.py
