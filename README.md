# ImSleepy

---
**NOTE**

This project is no longer maintained regularly.
Contributers and Creators are super busy :(

---

## Images
![ImSleepy](https://github.com/mrjoker05/ImSleepy/blob/master/Files/Image-01.png?raw=true)


## About
This is a program I created just because I am lazy.
<br>
It attends my online lectures for me ;)
<br>
Star this repo if it helped you. 
<br>
Contribute to make it better.
<br>
P.S If you are a faculty and somehow got this I'm sorry :p
<br>

## Requirements
1. Linux (Tested) or Windows (Beta)
2. Fast Internet ( Really Important )
3. Python 3.x
4. Chrome v85 above ( For windows )

## Setup
1. Navigate to the ```Files``` Directory
2. For Windows users: Run the Windows.sh file.
3. For Linux users: ```chmod +x Linux.sh && ./Linux.sh```
2. You can modify  your BlackBoard creds in the ```Files/Creds.txt``` file or can supply as an argument.

## Usage
```
usage: IamSleepy.py [-h] [--bg] [--list] [--timer TIMER] [--course COURSE] [--user USER] [--passw PASSW]

optional arguments:
  -h, --help       show this help message and exit
  --bg             Without Browser
  --list           List Course with number
  --timer TIMER    Stop Time
  --course COURSE  Course Number
  --user USER      BlackBoard Username
  --passw PASSW    BlackBoard Password

```
## Features
1. Can run fully in background
2. Set a timer to automatically close session
3. Raise hand, Writing to group chat ( In interactive mode )
4. Takes screenshots of session ( to prove that it's actually running )
5. [Add Time Table](https://github.com/mrjoker05/ImSleepy/blob/master/Files/Lazier.md) ( Beta Version )

## Testing and Contributions
A huge thanks to my friend [Aaryash](https://github.com/DirtyVibe) for testing this.
And [Anuj](https://github.com/Shinjiru-stack) for contributing.
<br>
This program was successfully tested on [Parrot GNU/Linux 4.10] [Ubuntu 18.04] [Kali 2020.3]
<br>

## Todos
- [x] Add minor error detection.
- [ ] Create a docker container for this program.
- [x] Make it fully run in the background.
- [x] Automate it a bit further by attaching timetable (A little buggy).
- [x] Run on windows

