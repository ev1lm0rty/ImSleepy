title I am Sleepy ...zzzz
@echo off


echo Currently Installed
wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value
echo WARNING: Please make sure you have chrome v85 installed before continuing'
pause

cls
:: Get BB Creds
set /p uservar="Enter Username: "
set /p passvar="Password: "
echo %uservar% > .\Files\Creds.txt
echo %passvar% >> .\Files\Creds.txt
echo Updated Credentials

cls
:: webdriver dependencies
echo Downloading chromedriver
::curl https://www.7-zip.org/a/7z1900-x64.exe -o 7z.exe
curl https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip -o driver.zip
7z e driver.zip 
echo done

cls
:: For setting up
echo installing python dependencies....
pip install selenium
pip install bs4
pip install lxml

cls
echo Start the Script from "StartHere.bat"
pause