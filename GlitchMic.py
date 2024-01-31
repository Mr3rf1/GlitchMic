# # STAN = Set Teams Auto-adjustment to Normal

# from __future__ import print_function
# from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
# import os


# def main():
    # sessions = AudioUtilities.GetAllSessions()

    # for session in sessions:
        # volume = session._ctl.QueryInterface(ISimpleAudioVolume)

        # if session.Process and session.Process.name() == "Teams.exe":
            # print("Teams audio is stabilized...")

            # volume.SetMasterVolume(0.18, None)
            # # 18% of system master volume
            

    # print("Microphone is being stabilized...")
    # os.system("nircmdc.exe loop 144000 250 setsysvolume 45875 default_record")
    # # nircmdc.exe loop /number of loops/ /time in ms to execute one loop/ setsysvolume /65536 == 100%/ /device/

    # print("Stabilization finished")


# if __name__ == "__main__":
    # main()

#!/usr/bin/env python3
"""Plot the live microphone signal(s) with matplotlib.

Matplotlib and NumPy have to be installed.

"""
# import argparse
# import queue
# import sys

# from matplotlib.animation import FuncAnimation
# import matplotlib.pyplot as plt
# import numpy as np
# import sounddevice as sd


# def int_or_str(text):
    # """Helper function for argument parsing."""
    # try:
        # return int(text)
    # except ValueError:
        # return text


# parser = argparse.ArgumentParser(add_help=False)
# parser.add_argument(
    # '-l', '--list-devices', action='store_true',
    # help='show list of audio devices and exit')
# args, remaining = parser.parse_known_args()
# if args.list_devices:
    # print(sd.query_devices())
    # parser.exit(0)
# parser = argparse.ArgumentParser(
    # description=__doc__,
    # formatter_class=argparse.RawDescriptionHelpFormatter,
    # parents=[parser])
# parser.add_argument(
    # 'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    # help='input channels to plot (default: the first)')
# parser.add_argument(
    # '-d', '--device', type=int_or_str,
    # help='input device (numeric ID or substring)')
# parser.add_argument(
    # '-w', '--window', type=float, default=200, metavar='DURATION',
    # help='visible time slot (default: %(default)s ms)')
# parser.add_argument(
    # '-i', '--interval', type=float, default=30,
    # help='minimum time between plot updates (default: %(default)s ms)')
# parser.add_argument(
    # '-b', '--blocksize', type=int, help='block size (in samples)')
# parser.add_argument(
    # '-r', '--samplerate', type=float, help='sampling rate of audio device')
# parser.add_argument(
    # '-n', '--downsample', type=int, default=10, metavar='N',
    # help='display every Nth sample (default: %(default)s)')
# args = parser.parse_args(remaining)
# if any(c < 1 for c in args.channels):
    # parser.error('argument CHANNEL: must be >= 1')
# mapping = [c - 1 for c in args.channels]  # Channel numbers start with 1
# q = queue.Queue()


# def audio_callback(indata, frames, time, status):
    # """This is called (from a separate thread) for each audio block."""
    # if status:
        # print(status, file=sys.stderr)
    # # Fancy indexing with mapping creates a (necessary!) copy:
    # q.put(indata[::args.downsample, mapping])


# def update_plot(frame):
    # """This is called by matplotlib for each plot update.

    # Typically, audio callbacks happen more frequently than plot updates,
    # therefore the queue tends to contain multiple blocks of audio data.

    # """
    # global plotdata
    # while True:
        # try:
            # data = q.get_nowait()
        # except queue.Empty:
            # break
        # shift = len(data)
        # plotdata = np.roll(plotdata, -shift, axis=0)
        # plotdata[-shift:, :] = data
    # for column, line in enumerate(lines):
        # line.set_ydata(plotdata[:, column])
    # return lines


# try:
    # if args.samplerate is None:
        # device_info = sd.query_devices(args.device, 'input')
        # args.samplerate = device_info['default_samplerate']

    # length = int(args.window * args.samplerate / (1000 * args.downsample))
    # plotdata = np.zeros((length, len(args.channels)))

    # fig, ax = plt.subplots()
    # lines = ax.plot(plotdata)
    # if len(args.channels) > 1:
        # ax.legend(['channel {}'.format(c) for c in args.channels],
                  # loc='lower left', ncol=len(args.channels))
    # ax.axis((0, len(plotdata), -1, 1))
    # ax.set_yticks([0])
    # ax.yaxis.grid(True)
    # ax.tick_params(bottom=False, top=False, labelbottom=False,
                   # right=False, left=False, labelleft=False)
    # fig.tight_layout(pad=0)

    # stream = sd.InputStream(
        # device=args.device, channels=max(args.channels),
        # samplerate=args.samplerate, callback=audio_callback)
    # ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=True)
    # with stream:
        # plt.show()
# except Exception as e:
    # parser.exit(type(e).__name__ + ': ' + str(e))
    
# import win32api
# WM_APPCOMMAND = 0x319

# APPCOMMAND_VOLUME_MAX = 0x0a
# APPCOMMAND_VOLUME_MIN = 0x09
# APPCOMMAND_MIC_ON_OFF_TOGGLE = 44
# APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

# win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * 0x10000)

# win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MIN * 0x10000)

# win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_MICROPHONE_VOLUME_MUTE * 0x10000)

import win32api
import win32gui
from time import sleep
from random import randint, uniform
from sys import argv

WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
APPCOMMAND_MICROPHONE_VOLUME_UP = 0x1a0000
APPCOMMAND_MICROPHONE_VOLUME_DOWN = 0x190000

hwnd_active = win32gui.GetForegroundWindow()

#for _ in range(50):
#    sleep(1)
    #win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_DOWN)
#    win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
#win32api.SendMessage(hwnd_active, WM_APPCOMMAND, 0x30292, APPCOMMAND_MICROPHONE_VOLUME_DOWN * 0x10000)
#exit(0)

def chst(vl):
    if vl == 'down':
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_DOWN)
    elif vl == 'up':
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
    print('changed')

def changeing():
    while True:
        # for _ in range(50): chst('down') # ghat
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        sleep(uniform(1.7, 3.0)) # time ghati
        # for _ in range(50): chst('up') # vals
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        sleep(uniform(0.3, 0.7)) # time vasli
        print('rounded')
        
     
if '-o' in argv:
    for _ in range(50):
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)# vals
    exit(0)
elif '-c' in argv:
    for _ in range(50):
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_DOWN)# vals
    exit(0)

#sleep(3)
#win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
print('fch')
for _ in range(50):
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
# mic aval kar vasl bashe
changeing()
# exit(0)

