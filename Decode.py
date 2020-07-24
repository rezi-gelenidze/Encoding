# Program that decodes code from encoding created by me into plain text
# Creator: Rezi Gelenidze
import os

# Character mapping
mapping = {
    '0': ['1234567890-=', '!@#$%^&*()_+'],
    '1': ['qwertyuiop[]\\','QWERTYUIOP{}|'],
    '2': ["asdfghjkl;\'", "ASDFGHJK""L:\""],
    '3': ['zxcvbnm,./', 'ZXCVBNM<>?']
}

banner ="\
 ____                     _       \n\
|  _ \  ___  ___ ___   __| | ___  \n\
| | | |/ _ \/ __/ _ \ / _` |/ _ \ \n\
| |_| |  __/ (_| (_) | (_| |  __/ \n\
|____/ \___|\___\___/ \__,_|\___| \n"

print(banner)

while True:
    # get input and check quit or clear commands
    inp = input("Enter code: ")
    
    # Check exit case
    if inp == '\q':
        break
    
    # Check clear command
    if inp == '\clear':
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(banner)
        continue    
    
    out = ''
    
    # split given string into separate codes
    inp = inp.split()
    
    try:
        # Decode each code
        for code in inp:
            row = code[0]
            char_case = int(code[-1])
            if len(code) == 4:
                index = int(code[1:3]) - 1
            else:
                index = int(code[1]) - 1

            char = mapping[row][char_case][index]
            out += char
    except:
        print("Invalid code.")

    # Print results
    print(out)