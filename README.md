# EV3-paper-plane-ontrol

This is a Lego EV3 Paper Airplane Launcher remote control via ssh.


## Build

First you nedd to build the EV3D4, or other, but the project is based on that model that is on the [EV3's webpage](https://www.lego.com/es-es/mindstorms/build-a-robot/ev3d4)

## Installl

**ev3dev**

For run this python program you will need [ev3dev](https://www.ev3dev.org)(a custom **dual-boot** firmware for your EV3) and a Wifi USB Dongle. Go [here](https://www.ev3dev.org/docs/getting-started/) to install.

**Install and run program**

Then of build your robot and install ev3dev, you need to install the program:

 1. First connect via ssh to your robot, here is a [tutorial](https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/)
 2. Then, clone the repository: `git clone https://github.com/Anti-Apple4life/EV3-paper-plane-control.git`
 3. Go into the directory you recently downloaded:`cd EV3-paper-plane-control`
 4. Run the script, `pyhton3 conbot.py`,and wait for it says *"LOG"*
 
 Here you have the function of all the keys(this list is thinked for view from back or from a camera, like a mobile phone):

|KEY|FUNCTION|
|--|--|
|w|Go forward|
|s|Go back|
|Space bar|Stop all motors|
|m|Play StarWars imperial march|
|q|Quit the program|

 5. For run the next time repeat the steps 1,3, and 4

 
