#!/bin/bash

# Get Creds
read -p 'Enter Username: ' uservar
read -p 'Password: ' passvar

echo $uservar > Files/Creds.txt
echo $passvar >> Files/Creds.txt

# For setting up
sudo apt update
sudo apt install python3-pip wget unzip awk -y
sudo wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo apt install ./*.deb -y --fix-missing
sudo wget "https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip" # Chrome Drvier
sudo unzip *.zip
rm -rf *.zip
dir=$(sudo echo $PATH | awk -F : '{print $1}')
sudo mv *driver* $dir
rm -rf *chrome*

# Python Modules
pip3 install selenium
pip3 install bs4
pip3 install lxml
