#coding=utf-8

import pyautogui
import pyperclip
import time
import cv2
import numpy as np
from PIL import ImageGrab

time.sleep(1)

load = 0
testplace = 0
print('請將DC全螢幕，並且把任何干擾畫面的視窗移開畫面')
print(pyautogui.size())

def Hist(gray):
    imgh = cv2.calcHist([gray], [0], None, [256], [0, 256])
    imgh = cv2.normalize(imgh, imgh, 0, 1, cv2.NORM_MINMAX, -1)
    return imgh

def test(screenshot):
    screenshotg = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_BGR2GRAY)
    img = cv2.imread('.\\IMG\\Epic_Guard.png', cv2.IMREAD_GRAYSCALE)
    screenshothist = Hist(screenshotg)
    imghist = Hist(img)
    similarity = cv2.compareHist(screenshothist, imghist, cv2.HISTCMP_CORREL)
    #cv2.imshow('show', screenshotg)
    #cv2.waitKey(0)
    if (0.0022 <= similarity <= 0.0035):
        time.sleep(1)
        print('\r', '處理中: 危險', end='')
        screenshot = ImageGrab.grab(bbox=(384, 829, 475, 943))
        screenshotg = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_BGR2GRAY)
        solve(screenshotg)
    print(similarity,end='')

def solve(screenshotg):
    _, screenshot_threshold = cv2.threshold(screenshotg, 36, 255, cv2.THRESH_BINARY)
    ''' 
    cv2.imshow("img", screenshot_threshold)  
    cv2.waitKey()  
    '''
    cnts, _ = cv2.findContours(screenshot_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(screenshotg,cnts,-1,(0,0,255),3)
    '''
    cv2.imshow("img", cnts)  
    cv2.waitKey(0)  
    print(len(cnts))
    '''

    print(len(cnts))
    cnt = cnts[len(cnts)-2]
    M = cv2.moments(cnt)
    print(M)
    if (M['m00'] > 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        screenshotg = screenshotg[cy-20:cy+20, cx-20:cx+20]
        _, img_threshold = cv2.threshold(screenshotg, 36, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(img_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cntsc = cnts[len(cnts)-2]
        #area = cv2.contourArea(cnt)
        '''     
        cv2.circle(screenshotg,(cx, cy),3,(0,255,0),-1)
        cv2.imshow("img", screenshotg)  
        cv2.waitKey(0) 
        ''' 
        print(cx, cy)
        memory = 1
        answer = 5
        for i in range(len(itemIMG)):
            img = cv2.imread(f'.\\IMG\\{itemIMG[i]}.png', cv2.IMREAD_GRAYSCALE)
            _, img_threshold = cv2.threshold(img, 36, 255, cv2.THRESH_BINARY)
            cnts, _ = cv2.findContours(img_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cntimg = cnts[len(cnts)-2]

            distance = cv2.matchShapes(cntsc, cntimg, 1, 0.0)
            '''         
            cv2.imshow("img", img_threshold)  
            cv2.waitKey()  
            '''
            '''
            cv2.imshow("img", img)  
            cv2.imshow("img2", screenshotg) 
            cv2.waitKey() 
            cv2.destroyAllWindows 
            '''
            screenshothist = Hist(screenshotg)
            imghist = Hist(img)
            similarity = cv2.compareHist(screenshothist, imghist, cv2.HISTCMP_BHATTACHARYYA)
            if (distance < memory):
                memory = distance
                answer = i
            print(distance)
        print(item[answer])
        pyperclip.copy(item[answer])
        pyautogui.hotkey('Ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')


while 1:
    item = ['normie fish', 'golden fish', 'epic fish', 'life potion', 'epic coin', 'coin', 'apple', 'banana', 'ruby', 'wolf skin', 'zombie eye', 'unicorn horn', 'mermaid hair', 'chip', 'dragon scale'] 
    itemIMG = ['Normie_fish', 'Golden_fish', 'Epic_fish', 'Life_potion_img', 'Epic_coin', 'Coin', 'Apple', 'Banana', 'Ruby_img', 'Wolf_skin_img', 'Zombie_eye_img', 'Unicorn_horn_img', 'Mermaid_hair_img', 'Chip_img', 'Dragon_scale_img']
    loading = ['[|]', '[\]', '[-]', '[/]']
    screenshot = ImageGrab.grab(bbox=(380, 773, 631, 802))
    test(screenshot)
    testplace += 1
    screenshot = ImageGrab.grab(bbox=(380, 835, 631, 863))
    test(screenshot)
    testplace = 0
    print(loading[load], '\r','偵測中: 安全',end='')
    if (load == 3):
        load = 0
    else:
        load += 1

#380, 773, 631, 802 0.00287
#380, 835, 631, 863 0.00329

#384, 829, 784, 943