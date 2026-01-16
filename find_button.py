import keyboard
import mouse
import time

#list with all characters on a normal keyboard
#do not include ` or \
#add more if you wish
characters = ['1','2','3','4','5','6','7','8','9','0',
              'q','w','e','r','t','y','u','i','o','p',
              'a','s','d','f','g','h','j','k','l',
              'z','x','c','v','b','n','m',
              '-','=','[',']',';',"'",',','.','/',
              'tab','caps lock','shift','ctrl','alt',
              'space','enter','backspace',
              'up','down','left','right']

def find_pressed():
    j=0
    for i in range(len(characters)):
        if keyboard.is_pressed(characters[j]):
            while keyboard.is_pressed(characters[j]):
                time.sleep(0.05)
            return characters[j]
        j+=1
    if mouse.is_pressed('left'):
        while mouse.is_pressed('left'):
            time.sleep(0.05)
        return 'mleft'
    elif mouse.is_pressed('right'):
        while mouse.is_pressed('right'):
            time.sleep(0.05)
        return 'mright'
    elif mouse.is_pressed('middle'):
        while mouse.is_pressed('middle'):
            time.sleep(0.05)
        return 'mmiddle'
    
    return None