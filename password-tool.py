import random, string, pyperclip, pynput, keyboard, colorama, os, subprocess, csv
from signal import SIGTERM
from pynput.keyboard import Key, Listener
from colorama import Fore, Back, Style

print(Fore.CYAN + 'Welcome to PG')

def PG():
    entered_num = int(input(Fore.LIGHTGREEN_EX + '1-Make a password with desired lengh\n2-Guess the possible passwords with your suggested words\n0-Quit'+ Fore.CYAN +'\nChoose to continue...'))

    if entered_num == 1:
        lengh = int(input(Fore.WHITE + 'enter your password lengh...'))
        g_password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation , k=lengh))
        print(Fore.RED + str(g_password) + Fore.WHITE + '\npress c to copy to your clipboard...')
        copy_password(g_password)
        print('please press enter to continue...')
        enter_to_continue()

    elif entered_num == 0:
        print(Fore.LIGHTYELLOW_EX + "Thank you to use Password_Tool!!!" + Fore.WHITE)
        quit()



#COPY THE GENERATED PASSWORD
def copy_password(g_pass):
    while True:
        key_pressed = keyboard.read_key()
        if key_pressed == 'c':
            pyperclip.copy(g_pass)
            print(Fore.RED + 'password copied!', end='')
            print(Fore.WHITE + '\npress enter to continue...', end='')
            input()
            PG()
        elif key_pressed == 'enter':
            enter_to_continue()
            print('press c to copy or enter to continue with out copy!', end='')
            copy_password(g_pass)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


#CONTINUE BY PRESSING ENTER
def enter_to_continue():
    if keyboard.read_key() == 'enter':
        input()
        PG()
    else:
        enter_to_continue()
PG()