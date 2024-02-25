#importing files to be used No.1

import reverseCipher
import caesarHacker 
import transpositionDecrypt
import transpositionFileHacker 
import os

#main program No.2

# Initialize variables
encrypted_message = ''
decrypted_message = ''
statistics_filename = " "
statistics_file = None
encrypted_message = []
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


filename = input("Enter file to be decrypted:")
    
try:                            #No.4 if the file exists, it opens in reading mode
    with open (filename, "r")as f:
        encrypt_messsage = f.readlines()
       
except IOError:                 # This means that the file does not exist (or some other IOError)
    print("Oops, file not found!")
    

if os.path.exists("decrypted_hfm.txt"):        #No.5 checking the file exists 
    print('Error: %s already exists.' %(decrypted_hfm.txt))
else:
    decrytpted_hfm = open(decrypted_hfm.txt, "w")    #open a new file storing decrypted message
    decrytpted_hfm.write()

# Create statistics filename
try:
    # Open the statistics file for writing
    statistics_file = open(statistics_filename, "w")
except IOError as e:
    print("Error: " + str(e))
    exit(1)

#No.6 beginning of decryption process
for line in encrypt_messsage:   #iterating line by line, the encrypted message
    line = line.strip()         #removing unneccessary space whitespace before and after the line

    decrypted_message = reverseCipher.reverse_message(line,key,symbols)   #attempting reverse cipher to decrpty the message
    if is_English(decrypted_message):   #checking if the result is english 
        decrytpted_hfm.write(decrypted_message + "/n")   #writing the results in the new file(decrypted_hfm.txt)
        continue  #if the decryption is unsuccessful, move on to transposition and ceasar 

    decrypted_message = transpositionFileHacker.hackTransposition(line)
    if decrypted_message is not None:
        decrytpted_hfm.write(decrypted_message + "/n")
        continue

    decrypted_message = caesarHacker.decrypt_message(line)
    if decrypted_message is not None:
        decrytpted_hfm.write(decrypted_message + "/n")
        continue

    decrytpted_hfm.write(decrypted_message + "/n")  #if non of the decrption works, write the text as is

filename.close()
decrypted_hfm.txt.close()
statistics_filename.close()



        
        
                
