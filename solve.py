"""
By: Richard Jooyeon -----
Description: circle script to solve vole problem.
Date: 5/18/2021
"""

import pyautogui
import math
import time

# when running this with vole:
""" Observations, I have noticed that getting to accurate results when drawing circle will result in error therefore we
must put human error when making the circle. see image: https://cdn.discordapp.com/attachments/563054518934437892/844281082728022097/unknown.png
or https://cdn.discordapp.com/attachments/836686156787744801/844287984571777054/unknown.png. This can be accomplished by 
putting slight resistance on the mouse or slightly shaking as circle is being made.
"""
time.sleep(2)  # delay for starting script

(X, Y) = pyautogui.position(pyautogui.size().width / 2, pyautogui.size().height / 2)  # get center position of screen.
radius = 300  # can change radius value accordingly.
pyautogui.moveTo(X + radius, Y)  # move mouse to right side of the center + radius.
# pyautogui.mouseDown()  # hold left mouse button down.
# Must turn off since complete automated process results in failure.
for i in range(366):  # each integer in 360 represents a degree in the cartesian grid.
    # 360+6 to take in consider overlap to complete circle.
    # We do not need complete circle since perfection results in error.
    if i % 6 == 0:  # represents every point in the unit circle
        pyautogui.moveTo(X + radius * math.cos(math.radians(i)),
                         Y + radius * math.sin(math.radians(i)))  # move to next value in the unit circle.
# pyautogui.mouseUp()  # lift left mouse button up.
# Must turn off since complete automated process results in failure.
