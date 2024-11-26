#import stuff#
import random
import time
import re
#add more if need be#
currentnumber = "00"
previousnumber = "00"
slot1 = "00"
slot2 = "00"
slot3 = "00"
slot4 = "00"
HCF = AREWEDOINGTHIS=False
inputbuffer = "00"
cue = "00"
done = "00"
AREWEDOINGTHIS = "False"
#commands themselves#
#ignore#
#How to see if user input is valid BASIC#
supported = ["PRINT", "RUN", "GOTO", "LIST"]
#Variable storage end#
"while" == "if"
print("RSB, but it may work now.")
while True:
    #userport = input()#
    print(" ")
    userport = input("RMB1.userport>: ")
    #now for the nested IFs#
    #Determine if user's code is to be listed or to be run after enter is hit#
    if userport[:2].isdigit():
        currentnumber = userport[:2]
        inputbuffer = userport[3:]
        if "PRINT" in userport and AREWEDOINGTHIS == "True":
            print(userport[9:])
            previousnumber = currentnumber
        if "10" in userport[:2]:
            slot1 = inputbuffer
            cue = slot1
        if "20" in userport[:2]:
            slot2 = inputbuffer
        if "30" in userport[:2]:
            slot3 = inputbuffer
        if "40" in userport[:2]:
            slot4 = inputbuffer
    else:
        if "PRINT" in userport:
            print(userport[6:])
        if "RUN" in userport:
            AREWEDOINGTHIS = "True"
            cue = slot1
            if "PRINT" in cue and AREWEDOINGTHIS == "True":
                print(cue[7:])
                AREWEDOINGTHIS = "False"
        if "LIST" in userport:
            print("10 " + slot1)
            print("20 " + slot2)
            print("30 " + slot3)
            print("40 " + slot4)