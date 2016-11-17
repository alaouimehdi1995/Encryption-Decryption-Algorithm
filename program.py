"""
Cryption/Decryption Algorithm, conceived and implemented by: ALAOUI Mehdi 2013
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

def crypt(initial_string):#Function that returns crypted value of initial_string
    crypted_string=""
    for i in range(len(initial_string)):
        CHARACTER_DELIMITER=chr(random.randint(97,109))
        FIRST_KEY=random.randint(2,10)
        SECOND_KEY=random.randint(2,16)
        t1=decimal_basis_to(ord(initial_string[i]),FIRST_KEY)
        CRYPTED_CHAR=decimal_basis_to(int(t1),SECOND_KEY)
        if(FIRST_KEY>9):
            FIRST_KEY=chr(FIRST_KEY+55) #adding 55 to have the ASCII code of character (ex: 10 -> 'A', 11 -> 'B')
        if(SECOND_KEY>9):
            SECOND_KEY=chr(SECOND_KEY+55)
        crypted_string+=CHARACTER_DELIMITER+str(FIRST_KEY)+str(SECOND_KEY)+CRYPTED_CHAR
    return(crypted_string)

def integer_value(CHAR_KEY): #Function that returns the integer value of a key (ex. '1'->1, 'B'->11)
    if(ord(CHAR_KEY)>=65):
        INT_KEY=int(ord(CHAR_KEY)-55)
    else:
        INT_KEY=int(CHAR_KEY)
    return(INT_KEY)

def reverse_basis (CRYPTED_NUMBER,KEY):
    decrypted_number=0
    n=len(str(CRYPTED_NUMBER))
    for i in range(n):
        CHARACTER_VALUE=integer_value(CRYPTED_NUMBER[i])
        decrypted_number+=CHARACTER_VALUE*(KEY**(n-1-i))
    return(str(decrypted_number))

def decrypt(CRYPTED_STRING):
    RESULT=""
    while(len(CRYPTED_STRING)>0):
        i=1
        while(i<len(CRYPTED_STRING) and ord(CRYPTED_STRING[i])<97):
            i+=1
        CRYPTED_SEQ=CRYPTED_STRING[1:i]
        CRYPTED_STRING=CRYPTED_STRING[i:]
        FIRST_KEY=CRYPTED_SEQ[0]
        SECOND_KEY=CRYPTED_SEQ[1]
        CRYPTED_CHAR=CRYPTED_SEQ[2:]
        CRYPTED_CHAR=reverse_basis(CRYPTED_CHAR,integer_value(SECOND_KEY)) #First Decryption
        RESULT+=chr(int(reverse_basis(CRYPTED_CHAR,integer_value(FIRST_KEY)))) #Second Decryption
    return(RESULT)

#MAIN PROGRAM
choix=1
while(choix!=0):    
    print("Would you crypt or decrypt ?")
    print("1- Crypt")
    print("2- Décrypt")
    print("0- Quit")
    choix=int(input())
    if(choix==1):
        print("Enter your text here to crypt it:")
        txt=str(input())
        result=crypt(txt)
        print(result)
        """fichier=open("cryptage.txt",'w')
        fichier.write("-- Crypted text: --\n\n")
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
