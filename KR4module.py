# Encode or decode with KR4 encoding system (Created by me)
# Created by: Rezi Gelenidze
# 25/07/20

# Character mapping
mapping = {
    '0': (
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+')
        ),
    '1': (
        ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'),
        ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|')
        ),
    '2': (
        ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"),
        ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"')
        ),
    '3': (
        ('z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'),
        ('Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?')
        )
    }


def encoder(inp):
    out = ''
    try:
        # Loop over each char in string and encode it
        for char in inp:
            if char == ' ':
                out += '123 '
                continue
            if char == '\n':
                out += '133 '
                continue
            code = ['','','', ' ']

            # Number 1 and 3
            for row, chars in mapping.items():
                for i in range(2):
                    if char in chars[i]:
                        code[0] = row
                        code[2] = str(i)

            # Number 2
            code[1] = str(
                mapping[code[0]][int(code[2])].index(char) + 1
                )
            # Join numbers
            out += ''.join(code)
    except:
        return None

    # return results
    return out


def decoder(inp):
    out = ''
    
    # split given string into separate codes
    inp = inp.split()
    
    try:
        # Decode each code
        for code in inp:
            if code == '123':
                out += ' '
                continue
            if code == '133':
                out += '\n'
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
        return None

    return out


if __name__ == '__main__':
    # tests
    plains = (
        'Hello',
        '123123',
        'How are you?'
        ' ',
        '',
        '!@#$%^&*()_+',
        'HELLo WORLd!!!',
        'He said: "Hello guys!"',
        'qazp\nlm10'
        )

    codes = (
        '261 130 290 290 190 ',
        '010 020 030 010 020 030 ',
        '261 190 120 123 210 140 130 123 160 190 170 3101 123 ',
        '',
        '011 021 031 041 051 061 071 081 091 0101 0111 0121 ',
        '261 131 291 291 190 123 121 191 141 291 230 011 011 011 ',
        '261 130 123 220 210 180 230 2101 123 2111 261 130 290 290 190 123 250 170 160 220 011 2111 ',
        '110 210 310 1100 133 290 370 010 0100 '
    )

    for plain, code in zip(plains, codes):
        if decoder(code) != plain:
            print('\033[91m' + f'DecodeError From {code} to {plain}')
        else:
            print('\033[92m' + 'Success!')

        if encoder(plain) != code:
            print('\033[91m' + f'EncodeError From {plain} to {code}')
        else:
            print('\033[92m' + 'Success!')
