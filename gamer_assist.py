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
            time.sleep(0.01)
        afterHold = time.time()
        timed = afterHold - beforeHold

        if timed < 0.4:
            keyboard.press('w')
            print("holding down w")
            while not keyboard.is_pressed('`'):
                time.sleep(0.01)
            keyboard.release('w')
            print("releasing w")
            while keyboard.is_pressed('`'):
                time.sleep(0.01)
        else:
            print('confirm button to mash')
            button = ''
            while not button:
                button = find_button.find_pressed()
                time.sleep(0.01)
            if button == '`' or button == '\\':
                print('cancelling')
            elif button[0] == 'm' and not len(button) == 1:
                mouseButton = button[1:]
                mouse.press(button=mouseButton)
                print(f"holding down {button}")
                while not keyboard.is_pressed('`'):
                    time.sleep(0.01)
                mouse.release(button=mouseButton)
                print(f"releasing {button}")
                while keyboard.is_pressed('`'):
                    time.sleep(0.01)
            else:
                keyboard.press(button)
                print(f"holding down {button}")
                while not keyboard.is_pressed('`'):
                    time.sleep(0.01)
                keyboard.release(button)
                print(f"releasing {button}")
                while not keyboard.is_pressed('`'):
                    time.sleep(0.01)
    #Auto masher
    if keyboard.is_pressed('\\'):
        beforeHold = time.time()
        while keyboard.is_pressed('\\'):
            time.sleep(0.01)
        afterHold = time.time()
        timed = afterHold - beforeHold

        if timed < 0.4:
            print("mashing mleft")
            while not keyboard.is_pressed('\\'):
                mouse.press(button='left')
                time.sleep(0.001)
                mouse.release(button='left')
                time.sleep(0.001)
            print("stopping mash mleft")
            while keyboard.is_pressed('\\'):
                time.sleep(0.01)
        else:
            print('confirm button to mash')
            button = ''
            while not button:
                button = find_button.find_pressed()
                time.sleep(0.01)
            if button == '`' or button == '\\':
                print('cancelling')
            elif button[0] == 'm' and not len(button) == 1:
                mouseButton = button[1:]
                print(f"mashing {button}")
                while not keyboard.is_pressed('\\'):
                    mouse.press(button=mouseButton)
                    time.sleep(0.001)
                    mouse.release(button=mouseButton)
                    time.sleep(0.001)
                print(f"stopping mash {button}")
                while keyboard.is_pressed('\\'):
                    time.sleep(0.01)
            else:
                print(f"mashing {button}")
                while not mouse.is_pressed('middle'):
                    keyboard.press(button)
                    time.sleep(0.001)
                    keyboard.release(button)
                    time.sleep(0.001)
                print(f"stopping mash {button}")
                while keyboard.is_pressed('\\'):
                    time.sleep(0.01)
    time.sleep(0.01)