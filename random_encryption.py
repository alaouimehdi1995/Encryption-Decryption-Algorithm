"""
Encryption/Decryption Algorithm, conceived and implemented by: ALAOUI Mehdi 2013
Code reviewed/cleaned: 2018
"""
import random

'''
RandomEncryption object is an 'API' to encrypt/decrypt string
useable methods:
    - encrypt(text, filename): returns a string containing encrypted value of 'text'
        if filename specified, will write the result in it.
    - encrypt_from_file(input_filename, output_filename): same use as 'encrypt' method, the first argument is a filename in which the text to encrypt will be read.

    - decrypt(text, filename): same use as 'encrypt' method, for decrypting.
    - decrypt_from_file(input_filename, output_filename): same use as 'encrypt_from_file', for decrypting.
'''

class RandomEncryption:

    def decrypt_from_file(self, input_filename: str, output_filename: str = None) -> str:
        text_to_decrypt = self._read(input_filename)
        return self.decrypt(text_to_decrypt, output_filename)


    def decrypt(self, text_to_decrypt: str, output_filename: str = None) -> str:
        decrypted_text = ''
        while len(text_to_decrypt) > 0:
            i = 1
            while i < len(text_to_decrypt) and ord(text_to_decrypt[i]) < 97:
                i += 1
            encrypted_sequence, text_to_decrypt = text_to_decrypt[1:i], text_to_decrypt[i:]
            first_basis, second_basis = (
                self._string_hex_to_int(encrypted_sequence[0]),
                self._string_hex_to_int(encrypted_sequence[1]),
            )
            char_to_decrypt = encrypted_sequence[2:]
            decrypted_char = self._revert_to_decimal_from_basis(first_basis,
                self._revert_to_decimal_from_basis(second_basis, char_to_decrypt)
            )
            decrypted_text += chr(int(decrypted_char))
        if output_filename:
            self._write(output_filename, decrypted_text)
        return decrypted_text

    def encrypt_from_file(self, input_filename: str, output_filename: str = None) -> str:
        text_to_encrypt = self._read(input_filename)
        return self.encrypt(text_to_encrypt, output_filename)

    def encrypt(self, text_to_encrypt: str, output_filename: str = None) -> str:
        encrypted_text = ''
        for char in text_to_encrypt:
            first_basis, second_basis = self._get_random_int(2, 10), self._get_random_int(2, 16)
            delimiter = self._get_random_char()
            encrypted_char = self._revert_from_decimal_to_basis(second_basis, int(
                self._revert_from_decimal_to_basis(first_basis, ord(char))
            ))
            first_basis = self._get_hex_value(first_basis)
            second_basis = self._get_hex_value(second_basis)
            encrypted_text += delimiter + first_basis + second_basis + encrypted_char
        if output_filename:
            self._write(output_filename, encrypted_text)
        return encrypted_text

    def _get_random_char(self, uppercase: bool = False):
        _ascii = self._get_random_int(65, 90) if uppercase else self._get_random_int(97, 122)
        return chr(_ascii)

    @staticmethod
    def _get_random_int(min_value: int, max_value: int) -> int:
        return random.randint(min_value, max_value)

    def _revert_from_decimal_to_basis(self, final_basis: int, number: int) -> str:
        output_value = ''
        while number > 0:
            (rest, number) = (number % final_basis, number // final_basis)
            rest = self._get_hex_value(rest)
            output_value = rest + output_value
        return output_value

    def _revert_to_decimal_from_basis(self, initial_basis: int, number: int) -> str:
        number, n = str(number), len(number)
        output_value = 0
        for index, digit in enumerate(number):
            digit_value = self._string_hex_to_int(digit)
            output_value += digit_value * (initial_basis ** (n - 1 - index))
        return str(output_value)

    @staticmethod
    def _string_hex_to_int(hexa_value: str) -> int:
        '''
        Returns integer value of a hexa string. Ex. '1' -> 1, 'B' -> 11.
        '''
        return int(hexa_value) if ord(hexa_value) < 65 else (ord(hexa_value) - 55)

    @staticmethod
    def _get_hex_value(int_value: int) -> str:
        return str(int_value) if int_value < 10 else chr(int_value + 55)

    @staticmethod
    def _read(filename):
        _file = open(filename, 'r')
        file_content = _file.read()
        _file.close()
        return file_content

    @staticmethod
    def _write(filename, value):
        _file = open(filename, 'w')
        _file.write(value)
        _file.close()
