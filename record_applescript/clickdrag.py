# on mouseDrag(xDown, yDown, xUp, yUp, delayTime)
# -- delayTime because the drag may fail if the UI isn't fast enough without a delay. For what I do, .1 works.
#    do shell script "
   
# /usr/bin/python
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventCreate
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import kCGEventLeftMouseDragged
import time

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy)

def mousedrag(posx,posy):
    mouseEvent(kCGEventLeftMouseDragged, posx,posy)

def mousedown(posxdown,posydown):
    mouseEvent(kCGEventLeftMouseDown, posxdown,posydown)

def mouseup(posxup,posyup):
    mouseEvent(kCGEventLeftMouseUp, posxup,posyup)

ourEvent = CGEventCreate(None)

# xDown = 19
# yDown = 153
# xUp = 978
# yUp = 632
# delayTime = 2

xDown = 19
yDown = 153
xUp = 499
yUp = 632
delayTime = 2

mousedown(xDown, yDown)
time.sleep(delayTime)
mousedrag(xUp, yUp)
time.sleep(delayTime)
mouseup(xUp, yUp)