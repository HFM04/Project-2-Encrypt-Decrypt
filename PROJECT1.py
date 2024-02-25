while True:
    encrypt_decrypt = input("encrypt (E) or decrypt (D)?:(E/D)  ").strip().lower()
    if not encrypt_decrypt:
        break
    if encrypt_decrypt not in ('e', 'd'):
        print("Please enter E/D!!""Please enter E/D!!")
        continue
    mode = input("String will be entered manually or retrieved from a file? (M :manually/F :file) ").strip().lower()
    if not mode:
        break
    if mode not in ('m', 'f'):
        print("Please enter M/F!!")
        continue
    try:
        if mode == 'm':
            input_string = input("Enter message: ")
        else:
            file = input("Enter file name: ")
            with open(filename, 'r') as f:
                input_string = f.read()
    except FileNotFoundError:
        print("File not found.")
        continue
    cipher = input("Do you want to use Reverse cipher or Ceasar cipher:(R/C)").strip().lower()
    if not cipher:
        break
    if cipher not in ('r', 'c'):
        print("Invalid input. Please enter R/")
        continue
    if cipher == 'c':
        key = int(input("Enter the key: "))
    if encrypt_decrypt == 'e':
        if cipher == 'r':
            output_string = input_string[::-1]
        else:
            output_string = ''.join([chr((ord(c) - 97 + key) % 26 + 97) if c.isalpha() else c for c in input_string])
    else:
        if cipher == 'r':
            output_string = input_string[::-1]
        else:
            output_string = ''.join([chr((ord(c) - 97 - key) % 26 + 97) if c.isalpha() else c for c in input_string])
    print("Output string: ", output_string)
