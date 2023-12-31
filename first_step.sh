#!/bin/bash

# gitがインストールされていることを確認
if ! command -v git &> /dev/null
then
    echo "gitがインストールされていません。先にインストールしてください。"
    exit 1
fi

sudo rosdep init 
rosdep update
git clone -b $ROS_DISTRO https://github.com/vstoneofficial/vs_rover_options_description.git

