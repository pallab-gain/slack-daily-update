FROM ubuntu:16.04

# Install necessary ubuntu packages
ARG slackurl
ARG channel
ARG email
ARG password


RUN apt-get update -y && apt-get install -y build-essential software-properties-common curl git htop man unzip vim wget python2.7 chromium-browser python-pip xvfb libgconf-2-4
RUN git clone https://github.com/pallab-gain/slack-daily-update.git --depth=1
RUN pip install virtualenv &&\
    bash slack-daily-update/dockerfiles/docker-helper.sh prepare_instance

ENV PYTHONPATH=${PYTHONPATH}:slack-daily-update

#CMD ["bash", "slack-daily-update/docker-helper.sh ${slackurl} ${channel} ${email} ${password}"]
