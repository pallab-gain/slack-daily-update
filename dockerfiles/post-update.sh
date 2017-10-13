#!/usr/bin/env bash

export slackurl=$1
export channel=$2
export email=$3
export password=$4
name='slack-daily-docker'
docker run -it --name ${slack-daily-docker} &\
    -e slackurl=$slackurl   &\
    -e channel=$channel &\
    -e email=$email &\
    -e password=$password   &\
    $name

