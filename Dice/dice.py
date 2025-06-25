import random
import os

def asciiConvert(num):
    num = list(str(num))
    for i in num:
        if (i == "0"):
            print(r'''
          _____
         /  _  \  
        /  /_\  \ 
        \  \_/  /
         \_____/''')
        if(i == "1"):
            print(r'''
         ____ 
        /_   |
         |   |
         |   |
         |___|''')
        elif(i == "2"):
            print(r'''
        ________  
        \_____  \ 
         /  ____/ 
        /       \ 
        \_______ \
                \/''')
        elif(i == "3"):
            print(r'''
        ________  
        \_____  \ 
          _(__  < 
         /       \
        /________/''')
        elif(i == "4"):
            print(r'''
           _____  
          /  |  | 
         /   |  |_
        /    ^   /
        \____   | 
             |__|''')
        elif(i == "5"):
            print(r'''
         .________
         |   ____/
         |____  \ 
         /       \
        /________/''')
        elif(i == "6"):
            print(r'''
          ________
         /  _____/
        /   __  \ 
        \  |__\  \
         \_______/''')
        elif(i == "7"):
            print(r'''
        _________ 
        \______  \
            /    /
           /    / 
          /____/''')
        elif(i == "8"):
            print(r'''
          ______  
         /  __  \ 
         >      < 
        /   --   \
        \________/''')
        elif(i == "9"):
            print(r'''
         ________ 
        /   __   \
        \____    /
           /    / 
          /____/''')
def quickDice(val):
    num = (random.randint(1, val))
    asciiConvert(num)
    os.system('pause')
def Dice(val):
    Redo = 1
    while Redo > 0:
        os.system('cls')
        DiceChoice = input(r'''###########################################
#                                         #
# ████████▄   ▄█   ▄████████    ▄████████ #
# ███   ▀███ ███  ███    ███   ███    ███ #
# ███    ███ ███▌ ███    █▀    ███    █▀  #
# ███    ███ ███▌ ███         ▄███▄▄▄     #
# ███    ███ ███▌ ███        ▀▀███▀▀▀     #
# ███    ███ ███  ███    █▄    ███    █▄  #
# ███   ▄███ ███  ███    ███   ███    ███ #
# ████████▀  █▀   ████████▀    ██████████ #
#                                         #
###########################################
by InYourWalls

Select:
1. Advantage (ADV)
2. Disadvantage (DIS)
3. None (NONE)
''')
        os.system('cls')
        a = (random.randint(1, val))
        b = (random.randint(1, val))
        if DiceChoice == '1' or DiceChoice.lower() == 'adv':    
            num = max(a,b)
            asciiConvert(num)
            os.system('pause')
        elif DiceChoice == '2' or DiceChoice.lower() == 'dis':
            num = min(a,b)
            asciiConvert(num)
            os.system('pause')
        elif DiceChoice == '3' or DiceChoice.lower() == 'none':
            num = a
            asciiConvert(num)
            os.system('pause')
        else:
            Redo += 1
        Redo -= 1
def isConvertibleToInt(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
def dryQuickDice(val):
    num = (random.randint(1, val))
    asciiConvert(num)
    print("\n\n\n\n\n") #adds 6 blank new lines to distinguish between throws
def dryAdvDice(val):
    a = (random.randint(1, val))
    b = (random.randint(1, val))
    num = max(a,b)
    asciiConvert(num)
    print("\n\n\n\n\n") #adds 6 blank new lines to distinguish between throws
def dryDisDice(val):
    a = (random.randint(1, val))
    b = (random.randint(1, val))
    num = min(a,b)
    asciiConvert(num)
    print("\n\n\n\n\n") #adds 6 blank new lines to distinguish between throws
def variedDiceTool():
    diceCode = input()
    diceCodeList = diceCode.split(" ")
    actualLenght = len(diceCode.strip("0123456789").split(" "))
    processedCode = [" "]*actualLenght
    
    i = 0
    while i < len(diceCodeList):
        if diceCodeList[i] == "roll":
            if isConvertibleToInt(diceCodeList[i+1]):
                processedCode[i] = int(diceCodeList[i+1])
                dryQuickDice(processedCode[i])
            else:
                print("Syntax Error")
                break
        elif diceCodeList[i] == "advroll":
            if isConvertibleToInt(diceCodeList[i+1]):
                processedCode[i] = int(diceCodeList[i+1])
                dryAdvDice(processedCode[i])
            else:
                print("Syntax Error")
                break
        elif diceCodeList[i] == "disroll":
            if isConvertibleToInt(diceCodeList[i+1]):
                processedCode[i] = int(diceCodeList[i+1])
                dryDisDice(processedCode[i])
            else:
                print("Syntax Error")
                break
        elif isConvertibleToInt(diceCodeList[i]):
            i += 1
            continue
        else:
            print("Syntax Error")
            break
        i += 1
    os.system('pause')
def printLogo():
    print(r'''###########################################
#                                         #
# ████████▄   ▄█   ▄████████    ▄████████ #
# ███   ▀███ ███  ███    ███   ███    ███ #
# ███    ███ ███▌ ███    █▀    ███    █▀  #
# ███    ███ ███▌ ███         ▄███▄▄▄     #
# ███    ███ ███▌ ███        ▀▀███▀▀▀     #
# ███    ███ ███  ███    █▄    ███    █▄  #
# ███   ▄███ ███  ███    ███   ███    ███ #
# ████████▀  █▀   ████████▀    ██████████ #
#                                         #
###########################################
by InYourWalls
''')
def main():
    while (True):
        os.system('cls')
        
        print(r'''###########################################
    #                                         #
    # ████████▄   ▄█   ▄████████    ▄████████ #
    # ███   ▀███ ███  ███    ███   ███    ███ #
    # ███    ███ ███▌ ███    █▀    ███    █▀  #
    # ███    ███ ███▌ ███         ▄███▄▄▄     #
    # ███    ███ ███▌ ███        ▀▀███▀▀▀     #
    # ███    ███ ███  ███    █▄    ███    █▄  #
    # ███   ▄███ ███  ███    ███   ███    ███ #
    # ████████▀  █▀   ████████▀    ██████████ #
    #                                         #
    ###########################################
    by InYourWalls
    ''')
        
        print(''' Select Tool:
    1.  Quick D4        8.  D4
    2.  Quick D6        9.  D6
    3.  Quick D8        10. D8
    4.  Quick D10       11. D10
    5.  Quick D12       12. D12
    6.  Quick D20       13. D20
    7.  Quick D100      14. D100

    15. Custom Quick Dice
    16. Custom Dice
    17. Varied Dice Tool

    0. Exit
        ''')
        
        choice = input()
        os.system('cls')
        if choice == '1':
            quickDice(4)
        elif choice == '2':
            quickDice(6)
        elif choice == '3':
            quickDice(8)
        elif choice == '4':
            quickDice(10)
        elif choice == '5':
            quickDice(12)
        elif choice == '6':
            quickDice(20)
        elif choice == '7':
            quickDice(100)
        elif choice == '8':
            Dice(4)
        elif choice == '9':
            Dice(6)
        elif choice == '10':
            Dice(8)
        elif choice == '11':
            Dice(10)
        elif choice == '12':
            Dice(12)
        elif choice == '13':
            Dice(20)
        elif choice == '14':
            Dice(100)
        elif choice == '15':
            printLogo()
            val = int(input("Select Custom Dice Number:"))
            os.system('cls')
            quickDice(val)
        elif choice == '16':
            printLogo()
            val = int(input("Select Custom Dice Number:"))
            os.system('cls')
            Dice(val)
        elif choice == '17':
            variedDiceTool()
        elif choice == '0' or choice.lower() == "exit":
            break

if __name__ == "__main__":
    main()

#All ASCII-art numbers based on https://patorjk.com/software/taag/#p=display&f=Graffiti&t=
#Big "DICE" text created using https://www.asciiart.eu/text-to-ascii-art

#  _____   
# /  _  \  
#/  /_\  \ 
#\  \_/  /
# \_____/

#_______   
#\   _  \  
#/  /_\  \ 
#\  \_/   \
# \_____  /
#       \/