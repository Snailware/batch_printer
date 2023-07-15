
import getpass as gp
import logging as log
from pathlib import Path

import pyautogui as pag

from Autoclicker import Autoclicker
from Timer import Timer


def main():
    
    NET_WEIGHT_FIELD_IMAGE_PATH: Path = Path.cwd() / "net_weight_field.PNG"
    pag.PAUSE: float = .08
    pag.FAILSAFE: bool = True
    INSTRUCTION_PROMPT: str = "this script will emulate mouse and keyboard events to print labels in bulk. it is meant to be used with non-fixed weight products in lieu of manually typing in weights repeatedly." +\
                              "\n\n" +\
                              "INSTRUCTIONS:" +\
                              "\n" +\
                              "1. open VNC and remote into scale, navigating to:" +\
                              "\n" +\
                              "Application Menu >> Carton Weighing >> Weigh/Print/Capture" +\
                              "\n" +\
                              "2. select [Change] in the bottom left corner of scale display, then enter and select the PLU of desired product to display weight entry prompt." +\
                              "\n" +\
                              "3. select [I Understand] below and enter desired label quantity and product weight when prompted." +\
                              "\n" +\
                              "4. confirm details on summary prompt, and select [Confirm] to begin printing." +\
                              "\n\n" +\
                              "!!! IMPORTANT !!!" +\
                              "\n" +\
                              "you can NOT use the computer as usual while this script is running. to abort script and stop execution immediately: move cursor to the top left corner of screen." +\
                              "\n\n" +\
                              "written and maintained by Adam Lancaster, 2022."

    user_acknowledgement = pag.confirm(text=INSTRUCTION_PROMPT,
                                       title="Bulk Label Printer Instructions",
                                       buttons=["I Understand", "Cancel"])
    if user_acknowledgement == "I Understand":

        quantity_to_print = pag.prompt(text="enter the number of labels you want to print:",
                                       title="enter label quantity")
        weight_to_print = pag.prompt(text="enter the weight you want printed on the labels:",
                                     title="enter product weight")
        user_confirmation = pag.confirm(text=f"is this info correct?\n\nlabel quantity:\t{quantity_to_print}\nproduct weight:\t{weight_to_print}",
                                        title="operation summary",
                                        buttons=["Confirm", "Cancel"])
        if user_confirmation == "Confirm":

            try:
                clicker: Autoclicker = Autoclicker()
                timer: Timer = Timer()
                log.basicConfig(filename="bulk_label_printer.log", 
                                filemode='a', 
                                format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s', 
                                level=log.INFO)
                timer.start()
                for i in range(0, int(quantity_to_print)):
                    clicker.find_and_click_center(NET_WEIGHT_FIELD_IMAGE_PATH)
                    clicker.enter_string(weight_to_print)
                timer.stop()

                log.info(f"{gp.getuser()} printed {quantity_to_print} labels in {timer.verbose_elapsed_time()}")
                pag.alert(f"Printing complete!\n\nQuantity printed: {quantity_to_print}\n\nElapsed time: {timer.verbose_elapsed_time()}")
            except(Exception):
                log.error(Exception)
    
    exit()

if __name__ == "__main__":
    main()