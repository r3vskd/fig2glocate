import curses
import keyboard
from colorama import Fore, Style, init
import sys
import time
import socket
import requests

init(autoreset=True)
def display_banner():
    print(Fore.RED + '''   
███████╗██╗ ██████╗ ██████╗  ██████╗ ██╗      ██████╗  ██████╗ █████╗ ████████╗███████╗
██╔════╝██║██╔════╝ ╚════██╗██╔════╝ ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝
█████╗  ██║██║  ███╗ █████╔╝██║  ███╗██║     ██║   ██║██║     ███████║   ██║   █████╗  
██╔══╝  ██║██║   ██║██╔═══╝ ██║   ██║██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  
██║     ██║╚██████╔╝███████╗╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                                                      
 Author: r3vskd                
 Warning: It was created for educational purposes. Please don't misuse it for illegal activities. 
          ''' + Style.RESET_ALL)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Please, choose a valid option"

def handle_option(stdscr, option):
    stdscr.clear()
    if option == 1:
        result = add(5, 5)
        stdscr.addstr(0, 0, f"Option 1: Add 5 + 5 = {result}")
    elif option == 2:
        result = subtract(10, 5)
        stdscr.addstr(0, 0, f"Option 2: Subtract 10 - 5 = {result}")
    elif option == 3:
        result = multiply(4, 3)
        stdscr.addstr(0, 0, f"Option 3: Multiply 4 * 3 = {result}")
    elif option == 4:
        stdscr.addstr(0, 0, "Option 4: Exit")
    elif option == 5:
        stdscr.addstr(0, 0, "Option 5: Go back to menu")

    stdscr.refresh()
    time.sleep(1)

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.addstr(0, 0, "☁ Press enter to select, or Esc to exit. ☁")
    stdscr.addstr(1, 0, "[01] ==> Substract the ip using the default ip-grabber redirection")
    stdscr.addstr(2, 0, "[02] ==> Retrieve the google maps location from an specific public ip address")
    stdscr.addstr(3, 0, "[03] ==> Substract the coordinates from an specific ip address")
    stdscr.addstr(4, 0, "[04] ==> Exit")
    stdscr.addstr(5, 0, "[05] ==> Go back to the main menu")
    stdscr.refresh()

    option = 1
    animate = False

    while True:
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            option = (option % 5) + 1
            stdscr.clear()
            stdscr.addstr(0, 0, "Scrolling")
            if animate:
                stdscr.addstr(0, 9, "...")
            stdscr.addstr(1, 0, "Selected option ==> " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  
            animate = not animate

        elif key == curses.KEY_UP:
            option = (option - 2) % 5 + 1
            stdscr.clear()
            stdscr.addstr(0, 0, "Scrolling")
            if animate:
                stdscr.addstr(0, 9, "...")
            stdscr.addstr(1, 0, "Selected option ==> " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  
            animate = not animate

        elif key == curses.KEY_ENTER or key in [10, 13]:
            handle_option(stdscr, option)
            if option == 4:
                break
            elif option == 5:
                stdscr.clear()
                stdscr.addstr(0, 0, "Returning to menu...")
                stdscr.refresh()
                time.sleep(1)
                stdscr.clear()
                stdscr.addstr(0, 0, "☁ Press enter to select, or Esc to exit. ☁")
                stdscr.addstr(1, 0, "[01] ==> Substract the ip using the default ip-grabber redirection")
                stdscr.addstr(2, 0, "[02] ==> Retrieve the google maps location from an specific public ip address")
                stdscr.addstr(3, 0, "[03] ==> Substract the coordinates from an specific ip address")
                stdscr.addstr(4, 0, "[04] ==> Exit")
                stdscr.addstr(5, 0, "[05] ==> Go back to the main menu")
                stdscr.refresh()
                option = 1

        elif key == 27: 
            stdscr.clear()
            stdscr.addstr(0, 0, "Exiting...")
            stdscr.refresh()
            time.sleep(1)  

if __name__ == "__main__":
    display_banner()
    curses.wrapper(main)