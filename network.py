import os
import time
import sys

ROOT_DIR = os.path.abspath(os.curdir)

host_file = open(ROOT_DIR + '/data/host.txt', 'r')
host_file_contents = host_file.read()

sec_file = open(ROOT_DIR + '/data/sec.txt', 'r')
sec_file_contents = sec_file.read()

method_file = open(ROOT_DIR + '/data/method.txt', 'r')
method_contents = method_file.read()

port_file = open(ROOT_DIR + '/data/port.txt', 'r')
port_file_contents = port_file.read()

user_file = open(ROOT_DIR + '/data/user.txt', 'r')
user_file_contents = user_file.read()
time.sleep(1)
os.system("cls")
print("")
print("")
print("")
print("")
print("                                                 \u001b[38;5;125m╔╗╔╔═╗╔╦╗╦\u001b[38;5;126m ╦╔═╗╦\u001b[38;5;127m═╗╦╔═")
print("                                                 \u001b[38;5;125m║║║║╣  ║ ║\u001b[38;5;126m║║║ ║╠\u001b[38;5;127m╦╝╠╩╗")
print("                                                 \u001b[38;5;125m╝╚╝╚═╝ ╩ ╚\u001b[38;5;126m╩╝╚═╝╩\u001b[38;5;127m╚═╩ ╩")
print("")
print("                                      \u001b[38;5;125m══════════════════\u001b[38;5;126m════════════\u001b[38;5;127m════════════")
print ("                                       \u001b[38;5;251mHost: " + host_file_contents)
print ("                                       \u001b[38;5;251mSeconds: " + sec_file_contents)
print ("                                       \u001b[38;5;251mMethod: " + method_contents)
print ("                                       \u001b[38;5;251mPort: " + port_file_contents)
print ("                                       \u001b[38;5;251mUser: " + user_file_contents)
print("                                      \u001b[38;5;125m══════════════════\u001b[38;5;126m════════════\u001b[38;5;127m════════════")
print("")
print("")
print("")
choice = input("\u001b[38;5;125m[" + user_file_contents + "\u001b[38;5;249m/\u001b[35;1m\u001b[38;5;127mlnNetWork]\u001b[38;5;249m$")
