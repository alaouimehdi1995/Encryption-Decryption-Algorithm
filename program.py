"""
Encryption/Decryption Algorithm, conceived and implemented by: ALAOUI Mehdi 2013
Code reviewed/cleaned: 2016
"""
import random
import os

def decimal_basis_to(NUMBER,BASIS): #Function that puts the number into the basis given in parameter
    result=""
    while(NUMBER!=0):
        REST=NUMBER%BASIS
        NUMBER=NUMBER//BASIS
        if(REST>9):
            REST=chr(REST+55) #adding 55 to have the ASCII code of character (ex: 10 -> 'A', 11 -> 'B')
        result=str(REST)+result
    return(result)

def encrypt(initial_string):#Function that returns encrypted value of initial_string
    encrypted_string=""
    for i in range(len(initial_string)):
        CHARACTER_DELIMITER=chr(random.randint(97,109))
        FIRST_KEY=random.randint(2,10)
        SECOND_KEY=random.randint(2,16)
        t1=decimal_basis_to(ord(initial_string[i]),FIRST_KEY)
        ENCRYPTED_CHAR=decimal_basis_to(int(t1),SECOND_KEY)
        if(FIRST_KEY>9):
            FIRST_KEY=chr(FIRST_KEY+55) #adding 55 to have the ASCII code of character (ex: 10 -> 'A', 11 -> 'B')
        if(SECOND_KEY>9):
            SECOND_KEY=chr(SECOND_KEY+55)
        encrypted_string+=CHARACTER_DELIMITER+str(FIRST_KEY)+str(SECOND_KEY)+ENCRYPTED_CHAR
    return(encrypted_string)

def integer_value(CHAR_KEY): #Function that returns the integer value of a key (ex. '1'->1, 'B'->11)
    if(ord(CHAR_KEY)>=65):
        INT_KEY=int(ord(CHAR_KEY)-55)
    else:
        INT_KEY=int(CHAR_KEY)
    return(INT_KEY)

def reverse_basis (ENCRYPTED_NUMBER,KEY):
    decrypted_number=0
    n=len(str(ENCRYPTED_NUMBER))
    for i in range(n):
        CHARACTER_VALUE=integer_value(ENCRYPTED_NUMBER[i])
        decrypted_number+=CHARACTER_VALUE*(KEY**(n-1-i))
    return(str(decrypted_number))

def decrypt(ENCRYPTED_STRING):
    RESULT=""
    while(len(ENCRYPTED_STRING)>0):
        i=1
        while(i<len(ENCRYPTED_STRING) and ord(ENCRYPTED_STRING[i])<97):
            i+=1
        ENCRYPTED_SEQ=ENCRYPTED_STRING[1:i]
        ENCRYPTED_STRING=ENCRYPTED_STRING[i:]
        FIRST_KEY=ENCRYPTED_SEQ[0]
        SECOND_KEY=ENCRYPTED_SEQ[1]
        ENCRYPTED_CHAR=ENCRYPTED_SEQ[2:]
        ENCRYPTED_CHAR=reverse_basis(ENCRYPTED_CHAR,integer_value(SECOND_KEY)) #First Decryption
        RESULT+=chr(int(reverse_basis(ENCRYPTED_CHAR,integer_value(FIRST_KEY)))) #Second Decryption
    return(RESULT)

#MAIN PROGRAM
choix=1
while(choix!=0):    
    print("Would you encrypt or decrypt ?")
    print("1- Encrypt")
    print("2- Decrypt")
    print("0- Quit")
    choix=int(input())
    if(choix==1):
        print("Enter your text here to encrypt it:")
        txt=str(input())
        result=encrypt(txt)
        print(result)
        """fichier=open("cryptage.txt",'w')
        fichier.write("-- Encrypted text: --\n\n")
        fichier.write(result)
        fichier.close()
        os.system("cryptage.txt")
        """
    elif(choix==2):
        print("Enter your text here to decrypt it:")
        txt=str(input())
        result=decrypt(txt)
        print(result)
        """fichier=open("decryptage.txt",'w')
        fichier.write("-- Decrypted text: --\n\n")
        fichier.write(result)
        fichier.close()
        os.system("decryptage.txt")
        """
