# Project1 solution - note this is ONE possible solution out of many; however, it does
#                            meet the expectations of the project.

###########################################################################################
# Define functions

def caesar(message, key, encrypt):

    # We'll need to share SYMBOLS from the main program, so define it as global
    global SYMBOLS
    
    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if encrypt == True:
                translatedIndex = symbolIndex + key
            else:
                translatedIndex = symbolIndex - key
                
            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
                
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    return translated

def reverse(message):
    # Reverse Cipher
    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    return translated

##################################################################
# The main program starts here

# (1) Initialize variables
# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.#'

# Start an infinite while loop
while True:
    
    # (2) Ask whether the program encrypts or decrypts;
    while True:
        encrypt = input('\nEnter a mode (1 = Encrypt, 0 = Decrypt) or press Enter to quit: ')
        if encrypt == '':
            break                       # Break the inner loop. You have one more loop to quit.
    # (3) Convert response to Boolean
        if encrypt in ['0','1']:        # if mode is 0 or 1
                encrypt = bool(int(encrypt)) # convert it to Boolean
                break                   # and break out of loop
                                        # otherwise, try again
    if encrypt == '':                      # Check to see if user wants to quit.
        break                           # Break the outer loop.
    
    # (4) Ask whether data entered manually or from a file
    while True:
        entry = input('Enter source type: (M)anual, (F)ile ')
        if entry.upper() == 'M':        # Manual == True
            entry = True
            break
        elif entry.upper() == 'F':      # File == False
            entry = False
            break

    # (5) Get data from appropriate source and store in input_string
    if entry == True:
        input_string = input('Please input a message:')
    else:
        fname = input('Enter filename: ')
        try:
            file = open(fname, "r")
            input_string = file.read()
        except IOError:                 # This means that the file does not exist (or some other IOError)
            print("Oops, file not found!")
            input_string = ''           # Since file not opened properly, there's nothing to process!

    # Only do the following if input_string is not empty

    if len(input_string) > 0:
        # (6) Ask which cipher to use, then...
        # (7) call the appropriate function, passing all necessary parameters
        cipher = input('Use which cipher? (C)aesar, (R)everse: ')
        if cipher.upper() == 'C':        # They want Caesar
        # (8) Get the caesar key, then call the caesar function
            while True:
                key = input('Enter key (value from 1 to %s): ' % len(SYMBOLS))
                try:
                    key = int(key)
                    if key >=1 and key <= len(SYMBOLS):
                        result = caesar(input_string, key, encrypt)
                        break
                    else:
                        print('Invalid key')
                except:
                    print('Invalid key')
        elif cipher.upper() == 'R':      # They want Reverse
            result = reverse(input_string)
        else:
            print("Invalid cipher!")

        # (9) Print the translated string
        print(result)

# Let user know program is done.
print("Stop program.")
