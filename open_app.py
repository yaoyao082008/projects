from msilib.schema import Control
import subprocess
from pynput.keyboard import Key , Controller
from pynput.mouse import Controller as C
from pynput.mouse import Button as B
import time
subprocess.call('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
x=450
y=135
keyboard=Controller()
mouse=C()
time.sleep(1)
keyboard.type('quizlet.com')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
mouse.position=(x,y)
time.sleep(2.5)
mouse.click(B.left)
time.sleep(1.5)
mouse.move(0,35)
mouse.click(B.left)
time.sleep(1.5)
Terms=['Studies','Evidence','Bioogy','Life','Cell']
for i in range(len(Terms)):
    mouse.scroll(0,-200)
    time.sleep(.4)
    mouse.move(0,145)
    mouse.click(B.left)
    time.sleep(.75)
    keyboard.type(Terms[0])
    time.sleep(0.75)
    mouse.move(500,0)
    mouse.click(B.left)
    time.sleep(0.75)
    mouse.move(0,80)
    time.sleep(0.75)
    mouse.click(B.left)
    mouse.move(-500,-145)
