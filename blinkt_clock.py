from blinkt import *
from time import strftime

# [Lo/Hi] [1] [2] [3] [4] [5] [6] [AM/PM]

#Edit these values to change clock colors or brightness (v). Blinkt! default brightness is .2, max 1
r = 64
g = 64
b = 64
v = .05

set_clear_on_exit(False)
clear()
set_all(25, 25, 35, v)
show()

split_time = strftime('%H %M %p').split(' ')
time_hour = int(split_time[0])
time_minute = int(split_time[1])

#Set the Lo/Hi and AM/PM bits 
if  time_hour > 12:
    set_pixel(0, 0, g, 0, v)
else:
    set_pixel(0, 0, 0, 0)

if split_time[2] == 'PM':
    set_pixel(7, 0, g, 0, v)

#Check for hour/minute overlap and set accordingly
minute_pixel = int(round(time_minute, -1) / 10)
hour_pixel = time_hour % 6 if time_hour % 6 > 0 else 6 

if minute_pixel == 0: 
    set_pixel(hour_pixel, 0, 0, b, v*2)
elif minute_pixel != hour_pixel:
    set_pixel(minute_pixel, r, 0, 0, v)
    set_pixel(hour_pixel, 0, 0, b, v)
else:
    set_pixel(minute_pixel, r, 0, b, v)

show()

