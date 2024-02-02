

# if __name__ == "__main__":
    # main()

#!/usr/bin/env python3
"""Plot the live microphone signal(s) with matplotlib.

Matplotlib and NumPy have to be installed.

"""
from os import name
from time import sleep
from random import uniform
from sys import argv

if name == 'nt':
    # windows libs
    import win32api
    import win32gui
    hwnd_active = win32gui.GetForegroundWindow()
elif name == 'posix':
    # linux lib
    import alsaaudio


WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
APPCOMMAND_MICROPHONE_VOLUME_UP = 0x1a0000
APPCOMMAND_MICROPHONE_VOLUME_DOWN = 0x190000


print("""
  ▄████  ██▓     ██▓▄▄▄█████▓ ▄████▄   ██░ ██     ███▄ ▄███▓ ██▓ ▄████▄  
 ██▒ ▀█▒▓██▒ Mr ▓██▒▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒   ▓██▒▀█▀ ██▒▓██▒▒██▀ ▀█  
▒██░▄▄▄░▒██░3rf1▒██▒▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░   ▓██    ▓██░▒██▒▒▓█    ▄ 
░▓█  ██▓▒██░    ░██░░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██    ▒██    ▒██ ░██░▒▓▓▄ ▄██▒
░▒▓███▀▒░██████▒░██░  ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓   ▒██▒   ░██▒░██░▒ ▓███▀ ░
 ░▒   ▒ ░ ▒░▓  ░░▓    ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒   ░ ▒░   ░  ░░▓  ░ ░▒ ▒  ░
  ░   ░ ░ ░ ▒  ░ ▒ ░    ░      ░  ▒    ▒ ░▒░ ░   ░  ░      ░ ▒ ░  ░  ▒   
░ ░   ░   ░ ░    ▒ ░  ░      ░         ░  ░░ ░   ░      ░    ▒ ░░        
      ░     ░  ░ ░           ░ ░       ░  ░  ░          ░    ░  ░ ░      
                             ░                                  ░         
""")

def app():
    if name == 'nt':
        if '-u' in argv or '--up-volume' in argv:
            for _ in range(50):
                win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)# vals
            exit(0)
        elif '-d' in argv or '--down-volume' in argv:
            for _ in range(50):
                win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_DOWN)# vals
            exit(0)

        for _ in range(50):
                win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)

        while True:
            win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE) # disconnect mic
            sleep(uniform(1.7, 3.0)) # disconnected time
            win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE) # connect mic
            sleep(uniform(0.3, 0.7)) # connected time
            print('Glitched successfully')

    elif name == 'posix':
        mic = alsaaudio.Mixer('Capture')

        while True:
            mic.setvolume(0) # Set the microphone volume to 0%
            sleep(uniform(1.7, 3.0))
            mic.setvolume(100) # Set the microphone volume to 100%
            sleep(uniform(1.7, 3.0))
            print('Glitched successfully')

try: app()
except KeyboardInterrupt:
    if name == 'nt': 
        for _ in range(50): win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
    elif name == 'posix': 
        mic = alsaaudio.Mixer('Capture')
        mic.setvolume(100)
