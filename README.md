# Blinkt Clock
A clock using the Pimoroni Blinkt! 8-pixel LED strip for Raspberry Pi Zero W.

The clock uses all 8 pixels, indicates AM/PM, and is accurate to 10-minute increments.

## Pixel [0]

Indicates if the hour pixel is "lo" (1-6 inclusive) or "hi" (7-12 inclusive). This allows the hour pixel to overflow back to 1 independent of the AM/PM calculation.

## Pixels [1:6]

Indicate the hour (in blue) and the nearest 10-minute fraction of the hour (in red).

For example,

    3:11 = ... [R] [_] [B] [_] [_] [_] ...

    6:47 = ... [_] [_] [_] [_] [R] [B] ...
    
If the hour and minute pixels overlap, they will form a purple pixel. Pixel [6] will stay lit through X:59, no red pixel will light between X:00-X:04.

## Pixel [7]

Indicates AM or PM.
