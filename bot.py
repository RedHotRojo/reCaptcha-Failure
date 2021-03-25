from time import sleep
import PIL.ImageGrab # Get pixels
from pynput.mouse import Button, Controller as mController 
from pynput.keyboard import Key, Controller as kController
mouse = mController()
keyboard = kController()
def waitForColor(i_x, i_y, clr):
    a = (0, 0, 0)
    while a != clr:
        a = PIL.ImageGrab.grab().load()[i_x, i_y]
        sleep(0.01)
#Open Firefox
keyboard.press(Key.cmd)
keyboard.press("1")
keyboard.release(Key.cmd)
keyboard.release("1")
waitForColor(1579, 13, (12, 12, 13))
#Enter URL
keyboard.type("https://www.polltab.com/QrDpBlrVCvk")
keyboard.tap(Key.enter)
#Choose option
mouse.position = (712, 673) # Adjust to where ever the option is
waitForColor(712, 673, (242, 242, 242))
mouse.click(Button.left, 1)
#Click reCaptcha!!
mouse.position = (826, 753)
waitForColor(813, 758, (178, 178, 178)) # Adjust to where ever the checkbox is
mouse.click(Button.left, 1)
waitForColor(826, 755, (0, 158, 85))
#Done
mouse.position = (911, 830) # Scam them
mouse.click(Button.left, 1)
