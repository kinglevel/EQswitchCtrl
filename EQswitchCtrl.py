import argparse
from serial import *

"""
Dirty and quick script to send simple strings and commands for the EQswitch for astrophotography.
This can for example be used with APT via commandline.

Tip is to add your folder with python scripts to your %PATH.

after PATH is setup, in APT just type:
EQswitchCtrl.py -r a -p COM6

"""


#setup
arduino = Serial()
parser = argparse.ArgumentParser()

#arguments
parser.add_argument("-r", "--relay", required=True, help="relay textname ex a A b B c C d D....")
parser.add_argument("-p", "--comport", required=True, help="COM Port ex COM6")
parser.add_argument("-b", "--baudrate", required=False, default="115200", help="COM Baudrate")

args = parser.parse_args()


#COM port setup
arduino.timeout = 2
arduino.baudrate = args.baudrate
arduino.port = args.comport


#message
message = bytes(str.encode(args.relay))
ending = bytes(b"\r\n")


#execute
arduino.open()
print(arduino.readline())
arduino.write(message+ending)
print(arduino.readline())
arduino.close()
