
import getpass as gp
import logging as log
from pathlib import Path

import pyautogui as pag

from Autoclicker_OLD import Autoclicker
from Timer_OLD import Timer
from colorama import Fore, Style
from rich.progress import Progress


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
                              Fore.RED + Style.BRIGHT + "!!! IMPORTANT !!!" +\
                              "\n" +\
                              "you can NOT use the computer as usual while this script is running. to abort script and stop execution immediately: move cursor to the top left corner of screen." +\
                              "\n\n" +\
                              Style.RESET_ALL +\
                              Fore.GREEN + "written and maintained by Adam Lancaster, 2022." + Style.RESET_ALL

    print(INSTRUCTION_PROMPT)
    user_acknowledgement = 'y'
    user_acknowledgement = input(" > continue? Y/n ").lower()
    if user_acknowledgement == '' or user_acknowledgement == 'y':
        quantity_to_print = input(" > enter label quantity: ")
        weight_to_print = input(" > enter label weight: ")
        user_confirmation = 'y'
        user_confirmation = input(f" > is this correct? Y/n\n\tquantity: {quantity_to_print} \n\tweight: {weight_to_print}").lower()
        if user_confirmation == '' or user_confirmation == 'y':

            try:
                clicker: Autoclicker = Autoclicker()
                timer: Timer = Timer()
                log.basicConfig(filename='batch_printer.log', 
                                filemode='a', 
                                format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s', 
                                level=log.INFO)
                timer.start()
                for i in range(1, int(quantity_to_print)):
                    clicker.find_and_click(image_path=NET_WEIGHT_FIELD_IMAGE_PATH)
                    clicker.enter_string(input=weight_to_print, 
                                         overwrite=False)
                timer.stop()

                log.info(f'{gp.getuser()} printed {quantity_to_print} labels in {timer.verbose_elapsed_time()}')
                pag.alert(f'Printing complete!\n\nQuantity printed: {quantity_to_print}\n\nElapsed time: {timer.verbose_elapsed_time()}')
            except Exception as e:
                log.exception('an error occured: ')
    
    exit()

if __name__ == "__main__":
    main()