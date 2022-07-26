from tkinter import S
from turtle import right
from djitellopy import Tello
from threading import Thread
import cv2, math, time
import keyboard
#This imports necessary code modules

print("Welcome to DJI Ryze Tello Control Centre!")
print("                                         ")
print("#########################################")
print("                                         ")
print("How to control your drone:               ")
print("Press w to move forward                  ")
print("Press a to move left                     ")
print("Press s to move back                     ")
print("Press d to move right                    ")
print("Press 1 to take off                      ")
print("Press 0 to land                          ")
print("Press arrow up to go up                  ")
print("Press arrow down to go down              ")
#Displays the text above to show the controls

key = keyboard.is_pressed
#Here, we are shortening the function to make writing and editing the code easier

tello = Tello()

tello.connect()
#Here, we are connecting to the drone

tello.streamon()
#Here, we are turning on the drone's camera, which allows us to view its stream

frame_read = tello.get_frame_read()

def SpeedFast():
    if key == ord('1'):
        tello.takeoff()
        print("Drone taking off...")

    elif key == ord('0'):
        tello.land()
        print("Drone landing...")

    elif key == ord('w'):
        tello.move_forward(50)
        print("Drone moving forward...")

    elif key == ord('a'):
        tello.move_left(50)
        print("Drone moving left...")

    elif key == ord('s'):
        tello.move_back(50)
        print("Drone moving back...")

    elif key == ord('d'):
        tello.move_right(50)
        print("Drone moving right...")

    elif key == ord('Up'):
        tello.move_up(50)
        print("Drone moving up...")

    elif key == ord('Down'):
        tello.move_down(50)
        print("Drone moving down...")

    elif key == ord('Right'):
        tello.rotate_counter_clockwise(30)
        print("Drone rotating right")

    elif key == ord('Left'):
        tello.rotate_clockwise(30)
        print("Drone rotating left")

def SpeedMedium():
    if key == ord('1'):
        tello.takeoff()
        print("Drone taking off...")

    elif key == ord('0'):
        tello.land()
        print("Drone landing...")

    elif key == ord('w'):
        tello.move_forward(30)
        print("Drone moving forward...")

    elif key == ord('a'):
        tello.move_left(30)
        print("Drone moving left...")

    elif key == ord('s'):
        tello.move_back(30)
        print("Drone moving back...")

    elif key == ord('d'):
        tello.move_right(30)
        print("Drone moving right...")

    elif key == ord('Up'):
        tello.move_up(30)
        print("Drone moving up...")

    elif key == ord('Down'):
        tello.move_down(30)
        print("Drone moving down...")

    elif key == ord('Right'):
        tello.rotate_counter_clockwise(30)
        print("Drone rotating right")

    elif key == ord('Left'):
        tello.rotate_clockwise(30)
        print("Drone rotating left")

def SpeedSlow():
    if key == ord('1'):
        tello.takeoff()
        print("Drone taking off...")

    elif key == ord('0'):
        tello.land()
        print("Drone landing...")

    elif key == ord('w'):
        tello.move_forward(10)
        print("Drone moving forward...")

    elif key == ord('a'):
        tello.move_left(10)
        print("Drone moving left...")

    elif key == ord('s'):
        tello.move_back(10)
        print("Drone moving back...")

    elif key == ord('d'):
        tello.move_right(10)
        print("Drone moving right...")

    elif key == ord('Up'):
        tello.move_up(10)
        print("Drone moving up...")

    elif key == ord('Down'):
        tello.move_down(10)
        print("Drone moving down...")

    elif key == ord('Right'):
        tello.rotate_counter_clockwise(30)
        print("Drone rotating right")

    elif 30 == ord('Left'):
        tello.rotate_clockwise(30)
        print("Drone rotating left")

print("What speed would you like to fly the drone at?")
print("Select 1 for Slow")
print("Seelect 2 for Medium")
print("Select 3 for Fast")

inputSpeed = input("Select an option")

if inputSpeed == 1:
    SpeedSlow()

elif inputSpeed == 2:
    SpeedMedium()

elif inputSpeed == 3:
    SpeedFast()


#More changes coming soon!!









