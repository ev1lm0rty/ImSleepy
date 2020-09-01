#!/bin/bash

sudo apt install -y python3-pip
pip3 install selenium bs4
wget "https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz"
tar -xvf *gz
sudo mv geckodriver /bin
