#!/usr/bin/env xcrun swift
import Foundation

let kDelayUSec : useconds_t = 500_000

func DragMouse(from p0: CGPoint, to p1: CGPoint) {
    let mouseDown = CGEventCreateMouseEvent(nil, .LeftMouseDown,    p0, .Left)
    let mouseDrag = CGEventCreateMouseEvent(nil, .LeftMouseDragged, p1, .Left)
    let mouseUp   = CGEventCreateMouseEvent(nil, .LeftMouseUp,      p1, .Left)

    CGEventPost(.CGHIDEventTap, mouseDown)
    usleep(kDelayUSec)
    CGEventPost(.CGHIDEventTap, mouseDrag)
    usleep(kDelayUSec)
    CGEventPost(.CGHIDEventTap, mouseUp)
}

func main() {
    let args = UserDefaults.standardUserDefaults()

    let x  = CGFloat(args.integerForKey("x"))
    let y  = CGFloat(args.integerForKey("y"))
    let dx = CGFloat(args.integerForKey("dx"))
    let dy = CGFloat(args.integerForKey("dy"))

    let p0 = CGPointMake(x, y)
    let p1 = CGPointMake(x + dx, y + dy)

    DragMouse(from: p0, to: p1)
}

main()