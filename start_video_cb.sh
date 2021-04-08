#!\bin\sh
python more_video_control_cb.py&
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/test_fifo bigbuckbunny320p.mp4
