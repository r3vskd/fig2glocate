import curses
import keyboard
from colorama import Fore, Style, init
import sys
import time

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

def print_option(stdscr, option):
    stdscr.clear()
    stdscr.addstr(0, 0, "Selected option: " + str(option))
    stdscr.refresh()

def handle_option(stdscr, option):
    stdscr.clear()
    if option == 1:
        stdscr.addstr(0, 0, "Option 1 selected.")
    elif option == 2:
        stdscr.addstr(0, 0, "Option 2 selected.")
    elif option == 3:
        stdscr.addstr(0, 0, "Option 3 selected.")
    elif option == 4:
        stdscr.addstr(0, 0, "Option 4 selected.")
    elif option == 5:
        stdscr.addstr(0, 0, "Option 5 selected.")
    elif option == 6:
        stdscr.addstr(0, 0, "Option 6 selected.")
    elif option == 7:
        stdscr.addstr(0, 0, "Option 7 selected.")
    elif option == 8:
        stdscr.addstr(0, 0, "Exiting...")

    stdscr.refresh()
    time.sleep(1)  

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Menu! Press Enter to select, or Esc to exit.")
    stdscr.refresh()

    option = 1
    animate = False
    while True:
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            option = (option % 8) + 1
            stdscr.clear()
            stdscr.addstr(0, 0, "Scrolling")
            if animate:
                stdscr.addstr(0, 9, "...")
            stdscr.addstr(1, 0, "Selected option: " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  
            animate = not animate

        elif key == curses.KEY_UP:
            option = (option - 2) % 8 + 1
            stdscr.clear()
            stdscr.addstr(0, 0, "Scrolling")
            if animate:
                stdscr.addstr(0, 9, "...")
            stdscr.addstr(1, 0, "Selected option: " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  
            animate = not animate

        elif key == curses.KEY_ENTER or key in [10, 13]:
            handle_option(stdscr, option)
            if option == 8:
                break

        elif key == 27:  
            stdscr.clear()
            stdscr.addstr(0, 0, "Exiting...")
            stdscr.refresh()
            time.sleep(1)  
            break

if __name__ == "__main__":
    curses.wrapper(main)