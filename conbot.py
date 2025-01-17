#!/usr/bin/env python3
# so that script can be run from Brickman
import subprocess
import termios, tty, sys
from ev3dev.ev3 import *

# attach large motors to ports B and C, medium motor to port A
motor_left = LargeMotor('outC')
motor_right = LargeMotor('outB')

#==============================================
print("\n============To the order!============\n\n\n\n============LOG============\n")
#==============================================
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch

def marchaimp():
   subprocess.call(['python3', 'marchaImperial'])   
#==============================================

def fire():
   motor_a.run_timed(time_sp=3000, speed_sp=600)

#==============================================

def forward():
   motor_left.run_forever(speed_sp=450)
   motor_right.run_forever(speed_sp=450)

#==============================================

def back():
   motor_left.run_forever(speed_sp=-450)
   motor_right.run_forever(speed_sp=-450)
    
#==============================================

def stop():
   motor_left.run_forever(speed_sp=0)
   motor_right.run_forever(speed_sp=0)
   motor_a.run_forever(speed_sp=0)
#==============================================

while True:
   k = getch()
   print(k)
   if k == 'm':
     marchaimp()
   if k == 'g':
      forward()
   if k == 'w':
      back()
   if k == ' ':
      stop()
   if k == 'q':
      exit()
