import pyautogui as pag
from time import sleep
from pathlib import Path

from pyperclip import paste

import PIL


class Autoclicker:
    """
    an easy to use class for GUI manipulation.
    """

    def __init__(self, failsafe: bool = True, pause: float = 0.08) -> None:
        """
        Args:
            failsafe (bool, optional): pyautogui failsafe flag. moving the cursor to 0,0 (top left corner of screen) will stop execution. this should almost always be True. Defaults to True.
            pause (float, optional): period of time in seconds between pyautogui actions. Defaults to 0.08.
        """
        pag.FAILSAFE = failsafe
        pag.PAUSE = pause

    def find_and_click(
        self,
        image_path: Path,
        x_offset: int = 0,
        y_offset: int = 0,
        confidence: float = 0.9,
    ) -> None:
        """
        search screen for image and click on it, optionally applying to center of image before clicking.

        Args:
            image_path (Path): path to image to search screen for.
            x_offset (int, optional): x offset to apply from image center before clicking. Defaults to 0.
            y_offset (int, optional): y offset to apply from image center before clicking. Defaults to 0.
            confidence (float, optional): how precisely screen image must match image for positive match. Defaults to 0.9.

        Raises:
            Exception: if image cannot be located on screen after 50 tries (roughly 5 seconds with included .1 second delay).
        """
        failed_attempts = 0
        x, y = None, None
        while x == None or y == None:
            try:
                x, y = pag.locateCenterOnScreen(image_path, confidence=confidence)
            except:
                failed_attempts += 1
                sleep(0.1)
            if failed_attempts > 50:
                raise Exception("could not locate image on screen.")
        pag.moveRel(x_offset, y_offset)
        pag.click(x, y)

    def find_field_and_enter_string(
        self,
        input: str,
        image_path: Path,
        overwrite: bool = True,
        x_offset: int = 0,
        y_offset: int = 0,
        confidence: float = 0.9,
    ) -> None:
        self.find_and_click(
            image_path=image_path,
            x_offset=x_offset,
            y_offset=y_offset,
            confidence=confidence,
        )
        self.enter_string(input=input, overwrite=overwrite)

    def find_field_and_extract_string(
        self,
        image_path: Path,
        x_offset: int = 0,
        y_offset: int = 0,
        confidence: float = 0.9,
    ) -> str:
        self.find_and_click(
            image_path=image_path,
            x_offset=x_offset,
            y_offset=y_offset,
            confidence=confidence,
        )
        return self.extract_string()

    def enter_string(self, input: str, overwrite: bool = True) -> None:
        if overwrite:
            pag.hotkey("ctrl", "a")
            pag.press("backspace")
        pag.write(input)
        pag.press("enter")

    def extract_string(self) -> str:
        pag.hotkey("ctrl", "a")
        pag.hotkey("ctrl", "c")
        return paste()


if __name__ == "__main__":
    print("this file should not be run directly. it contains code used by other files.")
