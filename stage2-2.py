
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(1)
print('[*] Start!')

def press_space():
    print('Space')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

press_space()
print('[*] 3, 2, 1')
time.sleep(2.9)

for i in range(4):
    press_space() 
    time.sleep(0.54)

   
press_space()  
time.sleep(0.27)
press_space()
   
for i in range(2):
    time.sleep(0.54)
    press_space()   


time.sleep(0.36) 

for i in range(5):
    time.sleep(0.54)
    press_space()


