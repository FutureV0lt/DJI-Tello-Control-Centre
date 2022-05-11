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

while True:
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
        tello.move_left
        print("Drone moving left...")

    elif key == ord('s'):
        tello.move_back
        print("Drone moving back...")

    elif key == ord('d'):
        tello.move_right
        print("Drone moving right...")

    elif key == ord('Up'):
        tello.move_up
        print("Drone moving up...")

    elif key == ord('Down'):
        tello.move_down
        print("Drone moving down...")

#More coming soon!!