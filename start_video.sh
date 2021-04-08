# ECE5725 Thurs3:30 - Lab1
# ih258 and kes334

#!\bin\sh
python video_control.py&
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/test_fifo bigbuckbunny320p.mp4
