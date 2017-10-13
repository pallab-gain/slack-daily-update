#!/usr/bin/env bash

file_path='slack-daily-update'
env_path='sduenv'

function install_virtual_env(){
    pushd ${file_path}
    mkdir -p ${env_path}
    virtualenv --no-site-packages ${env_path}
    popd
}

function install_dependencies(){

    pushd ${file_path}
    #activate
    source ${env_path}/bin/activate
    pip install -r requirements.txt

    deactivate
    popd
}


prepare_instance(){
    echo "-> preparing container"
    install_virtual_env
    install_dependencies
}

run_container(){
    pushd ${file_path}
    source ${env_path}/bin/activate

    #run the program
    python src/slackme.py &\
    -slackurl $SLACK_URL &\
    -channel $CHANNEL &\
    -email $EMAIL &\
    -password $PASSWORD

    deactivate
    popd
}

export SLACK_URL=$2
export CHANNEL=$3
export EMAIL=$4
export PASSWORD=$5

#execute the function
$1
