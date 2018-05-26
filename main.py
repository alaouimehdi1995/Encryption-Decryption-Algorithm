'''
Implemented by: ALAOUI Mehdi 2013
Code reviewed/cleaned: 2018

Simple example of RandomEncryption's uses
'''
from random_encryption import RandomEncryption

STRING_TO_ENCRYPT = 'Hello world, I\'m Mehdi.'
STRING_TO_DECRYPT = None
FILENAME = 'encryption_test.txt'

#  1- Encryption:

STRING_TO_DECRYPT = RandomEncryption().encrypt(STRING_TO_ENCRYPT)
print('--- Encryption result ---')
print(STRING_TO_DECRYPT)
print('--- --- --- --- --- ---\n\n')

# 2- Decryption:

print('--- Decryption result ---')
print(RandomEncryption().decrypt(STRING_TO_DECRYPT))
print('--- --- --- --- --- ---\n\n')

# 3- File use:

print(f'--- Encryption result (also stored in {FILENAME} file) ---')
print(RandomEncryption().encrypt(STRING_TO_ENCRYPT, FILENAME))
print('--- --- --- --- --- ---\n\n')


print(f'--- Decryption result (read from {FILENAME} file) ---')
print(RandomEncryption().decrypt_from_file(FILENAME))
print('--- --- --- --- --- ---\n\n')
