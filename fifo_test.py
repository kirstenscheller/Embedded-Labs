#ECE5725 Thurs3:30 - Lab1
# ih258 and kes334

import os

playing = True

while(playing):
    x = raw_input("Press a for pause or 107 for quitting: " )
    if(x == 'a'):
        print("Paused")
        os.system('echo "pause" > /home/pi/test_fifo')
    elif(x == '107'):
        print("Quit")
        os.system('echo "q" > /home/pi/test_fifo')
        playing = False
