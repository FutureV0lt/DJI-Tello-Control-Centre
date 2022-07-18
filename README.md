# DJI-Tello-Control-Centre
Dji Tello Drone control centre built from damiafuentas' DJITelloPy python interface.

A simple DJI Ryze Tello control centre with basic functionality. More will be coming soon!!
This also enables the drone's camera and allows you to see it!

Note that I cannot test this out since I do not own the drone, but there are very high chances this will work. If it doesn't, do let me know and I will be more than happy to look into it and fix it.

# Usage:
- 1 to take off
- 0 to land
- w to move forward
- a to move left
- s to move back
- d to move right
- arrow up key to move up
- arrow down key to move down

## Windows installation of pip and requirements (if the .bat file doesn't work for whatever reason):
```
@echo off
echo Welcome to pip installer for DJI Ryze Tello!
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install keyboard
pip install djitellopy
```

# Android installation (Termux or alternative terminal emulator):
Copy and paste this code as is into your desired terminal emulator:
```
apt full-upgrade && apt update && apt-get install git && apt-get install python3 && pkg install python3 && pkg install git && pkg install python2 && git clone https://github.com/FutureV0lt/DJI-Tello-Control-Centre && pip install && pip install --upgrade && pip install djitellopy
```
Run this once the code is updated to get the latest version:
```
git clone https://github.com/FutureV0lt/DJI-Tello-Control-Centre
```


# There will be more features coming soon...
if you like this project, a star would be greatly appreciated ;)
