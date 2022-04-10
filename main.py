import pyautogui as pya
import time
import cv2
import os
os.system('open /Applications/Firefox.app')
time.sleep(1)
def AutoAid():
    x, y = pya.locateCenterOnScreen('/Users/zach/workspace/FOEMACRO~Zach/Next.png', grayscale=True)
    while True:
        count = 0
        for pos in pya.locateAllOnScreen('Aid.png', grayscale=True, confidence=0.8):
            if(pos[1] != 1316):
                continue
            time.sleep(.2)
            x1, y1 = pya.center(pos)
            pya.click(x1, y1)
            time.sleep(1)
            count += 1
        if count == 0:
            pya.press('g')
            time.sleep(1)
            pya.click(pya.locateCenterOnScreen('Members.png', grayscale=True)[0], pya.locateCenterOnScreen('Members.png', grayscale=True)[1])
            time.sleep(1)
            print(str(pya.size()[0]/2) + " " + str(pya.size()[1]/2))
            pya.scroll(10, pya.size()[0]/2, pya.size()[1]/2)
        hey = pya.locateOnScreen('Aid.png', grayscale=True, confidence=0.8)
        if hey == None:
            pya.click(x, y)
            time.sleep(.2)
        else: 
            print('wsg boiz')
            continue
            
    
if __name__ == '__main__':
    AutoAid()