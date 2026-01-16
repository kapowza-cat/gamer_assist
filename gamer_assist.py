import pyautogui
import time
import keyboard
import mouse
import find_button



print("Program active")

while True:
    #Auto holder
    if keyboard.is_pressed('`'):
        beforeHold = time.time()
        while keyboard.is_pressed('`'):
            time.sleep(0.05)
        afterHold = time.time()
        timed = afterHold - beforeHold

        if timed < 0.4:
            pyautogui.keyDown('w')
            print("holding down w")
            while not keyboard.is_pressed('`') or keyboard.is_pressed('w'):
                time.sleep(0.05)
            pyautogui.keyUp('w')
            print("releasing w")
        else:
            button = ''
            while not button:
                button = find_button.find_pressed()
                time.sleep(0.05)
            if button[0] == 'm' and not len(button) == 1:
                mouseButton = button[1:]
                pyautogui.mouseDown(button=mouseButton)
                print(f"holding down {button}")
                while not keyboard.is_pressed('`') or mouse.is_pressed(mouseButton):
                    time.sleep(0.05)
                pyautogui.mouseUp(button=mouseButton)
                print(f"releasing {button}")
            else:
                pyautogui.keyDown(button)
                print(f"holding down {button}")
                while not keyboard.is_pressed('`') or keyboard.is_pressed(button):
                    time.sleep(0.05)
                pyautogui.keyUp(button)
                print(f"releasing {button}")
    time.sleep(0.05)