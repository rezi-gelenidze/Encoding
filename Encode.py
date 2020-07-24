# Program that encodes text with encoding created by me
# Creator: Rezi Gelenidze
import os

banner = "\
 _____                     _       \n\
| ____|_ __   ___ ___   __| | ___  \n\
|  _| | '_ \ / __/ _ \ / _` |/ _ \ \n\
| |___| | | | (_| (_) | (_| |  __/ \n\
|_____|_| |_|\___\___/ \__,_|\___| \n\
"

mapping = {
    '0': ['1234567890-=!@#$%^&*()_+', 12],
    '1': ['qwertyuiop[]\QWERTYUIOP{}|', 13],
    '2': ["asdfghjkl;\'ASDFGHJK""L:\"", 11],
    '3': ['zxcvbnm,./ZXCVBNM<>?', 10]
}

upchars = "!@#$%^&*()_+{}|:\"<>?"
lowchars = "1234567890-=[]\\;\',./"

print(banner)

while True:
    inp = input("Enter Text: ")
    out = ''

    # Check exit case
    if inp == '\q':
        break
    
    # Check clear command
    if inp == '\clear':
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(banner)
        continue

    # Loop over each char in string and encode it
    for char in inp:
        code = ['','','','\n']

        # Number 1
        for i in mapping:
            if char in mapping[i][0]:
                code[0] = i

        # Number 3
        if char.isupper() or char in upchars:
            code[2] = '1'
        elif char.islower() or char in lowchars:
            code[2] = '0'
        else:
            continue
        
        # Number 2
        row = code[0]

        num2 = (mapping[row][0].find(char) + 1) % mapping[row][1]
        
        if num2 == 0:
            code[1] = '1'
        else:
            code[1] = str(num2)

        # Join numbers
        out += ''.join(code)

    # Print results
    print(out)
