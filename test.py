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
        return "Error: Division by zero"

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
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Menu! Press Enter to select, or Esc to exit.")
    stdscr.addstr(1, 0, "1. Add")
    stdscr.addstr(2, 0, "2. Subtract")
    stdscr.addstr(3, 0, "3. Multiply")
    stdscr.addstr(4, 0, "4. Exit")
    stdscr.addstr(5, 0, "5. Go back to the main menu")
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
            stdscr.addstr(1, 0, "Selected option: " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  # Wait for 0.2 seconds for animation
            animate = not animate

        elif key == curses.KEY_UP:
            option = (option - 2) % 5 + 1
            stdscr.clear()
            stdscr.addstr(0, 0, "Scrolling")
            if animate:
                stdscr.addstr(0, 9, "...")
            stdscr.addstr(1, 0, "Selected option: " + str(option))
            stdscr.refresh()
            time.sleep(0.2)  # Wait for 0.2 seconds for animation
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
                stdscr.addstr(0, 0, "Welcome to the Menu! Press Enter to select, or Esc to exit.")
                stdscr.addstr(1, 0, "1. Add")
                stdscr.addstr(2, 0, "2. Subtract")
                stdscr.addstr(3, 0, "3. Multiply")
                stdscr.addstr(4, 0, "4. Exit")
                stdscr.addstr(5, 0, "5. Go back to the main menu")
                stdscr.refresh()
                option = 1

        elif key == 27:  # ESC key
            stdscr.clear()
            stdscr.addstr(0, 0, "Exiting...")
            stdscr.refresh()
            time.sleep(1)  # Sleep for 1 second for animation
            break

if __name__ == "__main__":
    display_banner()
    curses.wrapper(main)