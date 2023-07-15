import pyautogui as pag
from time import sleep
from pathlib import Path

import PIL

class Autoclicker:
    def __init__(self, failsafe:bool=True, pause:float=0.08) -> None:
        pag.FAILSAFE = failsafe
        pag.PAUSE = pause

    def find_and_click_center(self, image_path:Path) -> None:
        failed_attempts = 0
        x, y = None, None
        while x == None or y == None:
            try:
                x, y = pag.locateCenterOnScreen(str(image_path), confidence=0.9)
            except:
                failed_attempts += 1
                sleep(.1)
            if failed_attempts > 50: raise Exception("could not locate image.")
        pag.click(x, y)

    def enter_string(self, string:str) -> None:
        pag.write(string)
        pag.press('enter')

    def get_string(self) -> str:
        pass

if __name__ == '__main__':
    print("this file should not be run directly. it contains code used by other files.")