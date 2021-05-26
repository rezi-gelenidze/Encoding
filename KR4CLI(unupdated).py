# Encode or decode with KR4 encoding system (Created by me)
# Created by: Rezi Gelenidze
# 25/07/20
import os

# Banners
banner_main = "\
 _  ______  _  _                              _           \n\
| |/ /  _ \| || |     ___ _ __   ___ ___   __| | ___ _ __ \n\
| ' /| |_) | || |_   / _ \ '_ \ / __/ _ \ / _` |/ _ \ '__|\n\
| . \|  _ <|__   _| |  __/ | | | (_| (_) | (_| |  __/ |   \n\
|_|\_\_| \_\  |_|    \___|_| |_|\___\___/ \__,_|\___|_|   \n"
                                                         

banner_encode = "\
 _____                     _       \n\
| ____|_ __   ___ ___   __| | ___  \n\
|  _| | '_ \ / __/ _ \ / _` |/ _ \ \n\
| |___| | | | (_| (_) | (_| |  __/ \n\
|_____|_| |_|\___\___/ \__,_|\___| \n"

banner_decode ="\
 ____                     _       \n\
|  _ \  ___  ___ ___   __| | ___  \n\
| | | |/ _ \/ __/ _ \ / _` |/ _ \ \n\
| |_| |  __/ (_| (_) | (_| |  __/ \n\
|____/ \___|\___\___/ \__,_|\___| \n"

# Character mapping
mapping = {
    '0': ['1234567890-=', '!@#$%^&*()_+'],
    '1': ['qwertyuiop[]\\','QWERTYUIOP{}|'],
    '2': ["asdfghjkl;\'", "ASDFGHJK""L:\""],
    '3': ['zxcvbnm,./', 'ZXCVBNM<>?']
}

menu = "[1] Encode\n[2] Decode"

def main():
    print(banner_main)

    while True:
        print(menu)

        inp = input("Select operation:")

        if inp == "\q":
            exit()
        elif inp == '1':
            encoder()
        elif inp == '2':
            decoder()
        elif inp == '':
            clear()
            print(banner_main)
            continue
        else:
            print("Invalid input.")
            continue

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 

def check_quit(user_input):
    if user_input == "\q":
        clear()
        exit()

def encoder():
    clear()
    print(banner_encode)

    while True:
        inp = input("Enter Text: ")
        out = ''

        # Check back to menu case
        if inp == '\\b':
            clear()
            print(banner_main)
            break

        # Check quit case
        check_quit(inp)

        # Check clear command
        if inp == '\clear':
            clear()
            continue

        try:
            # Loop over each char in string and encode it
            for char in inp:
                if char == ' ':
                    out += '123\n'
                    continue
                code = ['','','','\n']

                # Number 1 and 3
                for row, chars in mapping.items():
                    for i in range(2):
                        if char in chars[i]:
                            code[0] = row
                            code[2] = str(i)

                # Number 2
                row = code[0]
                charcase = int(code[2])

                code[1] = str(mapping[row][charcase].find(char) + 1)

                # Join numbers
                out += ''.join(code)
        except:
            print(f"Invalid input.")
            continue

        # Print results
        print(out)

def decoder():
    clear()
    print(banner_decode)

    while True:
        # get input and check quit or clear commands
        inp = input("Enter code: ")
        
        # Check back case
        if inp == '\\b':
            clear()
            print(banner_main)
            break
        
        # Check quit case
        check_quit(inp)

        # Check clear command
        if inp == '\clear':
            clear()      
            print(banner_decode)
            continue    
        
        out = ''
        
        # split given string into separate codes
        inp = inp.split()
        
        try:
            # Decode each code
            for code in inp:
                if code == '123':
                    out += ' '
                    continue
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

if __name__ == "__main__":
    main()
