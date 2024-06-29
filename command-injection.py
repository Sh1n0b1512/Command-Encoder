#!/bin/bash/python3

import sys
import urllib.parse
from colorama import Fore

intro = '\n\tURL Encoder for Linux Command Injection Payload\n'

required_arguments = 1
if len(sys.argv) - 1 < required_arguments:
    print(Fore.BLUE + "\t\nThis script requires at least one argument.\n")
    print(Fore.BLUE + "The argument is the command you want to encode.\n")
    sys.exit(1)
elif len(sys.argv) -1 > required_arguments:
    print(Fore.BLUE + "Enter one command at a time.\n")
    sys.exit(1)
else:
    print(Fore.BLUE + intro)

chars = [':',';','`','?','^',';','$','#','@','||','|','!','&','&&']
command = sys.argv[1]
print(Fore.BLUE + "Encoding command: " + Fore.GREEN + command)

def command_encoder(command):
    for char in chars:
        print(urllib.parse.quote(command + char))
        print(urllib.parse.quote(char + command))
        print(urllib.parse.quote(char + command + char))
        
if __name__ == '__main__':
    command_encoder(command)

