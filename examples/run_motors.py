"""
    run_motors.py

    This micro:bit MicroPython script uses k_motor.py to run 2 motors connected to
    the kitronik motor driver board.

    https://www.kitronik.co.uk/5620-motor-driver-board-for-the-bbc-microbit-v2.html

    The MIT License (MIT)

    Copyright (c) 2018 Alan Yorinks

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from k_motor import KMotor
from microbit import sleep

# create an instance of KMotor
r = KMotor()

# turn motor 1 on in forward for 1 second and turn it off
r.motor_on(r.MOTOR_1, r.FORWARD, 100)
sleep(1000)
r.motor_off(r.MOTOR_1)

# turn motor 1 on in reverse for 1 second and turn it off
r.motor_on(r.MOTOR_1, r.REVERSE, 100)
sleep(1000)
r.motor_off(r.MOTOR_1)

# turn motor 2 on in forward for 1 second and turn it off
r.motor_on(r.MOTOR_2, r.FORWARD, 100)
sleep(1000)
r.motor_off(r.MOTOR_2)

# turn motor 2 on in reverse for 1 second and turn it off
r.motor_on(r.MOTOR_2, r.REVERSE, 100)
sleep(1000)
r.motor_off(r.MOTOR_2)

# spin 1 - spin motors 1 and 2 in opposite directions for 2 seconds
r.motor_on(r.MOTOR_1, r.FORWARD, 100)
r.motor_on(r.MOTOR_2, r.REVERSE, 100)
sleep(2000)
r.motor_off(r.MOTOR_1)
r.motor_off(r.MOTOR_2)


# spin 2 - spin motors 1 and 2 in opposite directions for 2 seconds
# but changing the directions of the motors from the previous run
r.motor_on(r.MOTOR_2, r.FORWARD, 100)
r.motor_on(r.MOTOR_1, r.REVERSE, 100)
sleep(2000)
r.motor_off(r.MOTOR_1)
r.motor_off(r.MOTOR_2)

# turn both motors on in forward for a second
r.motor_on(r.MOTOR_1, r.FORWARD, 100)
r.motor_on(r.MOTOR_2, r.FORWARD, 100)
sleep(1000)

# without pause # turn both motors on in reverse for a second
r.motor_on(r.MOTOR_1, r.REVERSE, 100)
r.motor_on(r.MOTOR_2, r.REVERSE, 100)
sleep(1000)

# turn both motors off
r.motor_off(r.MOTOR_1)
r.motor_off(r.MOTOR_2)