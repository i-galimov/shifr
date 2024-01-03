# Написать программу, которая шифрует файл/пользовательский ввод в консоль

'''
1. Считать из клавы/файла
2. Алгоритм шифрования:
- base64
- перевернуть задом наперед
- разделим на две части, и переставим местами
- сдвинем текст по алгоритму цезаря
'''

import base64
import os

def encode_base64(message):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message  # Return the decoded text

def decode_base64(encoded_text):
    # Convert the base64 encoded text to bytes
    decoded_bytes = base64.b64decode(encoded_text)
    # Convert the bytes to a string using UTF-8 encoding
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text  # Return the decoded text

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # проверяем, является ли символ буквой
            shift_amount = 65 if char.isupper() else 97  # определяем смещение для верхнего или нижнего регистра
            shifted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)  # смещаем символ
            result += shifted_char
        else:
            result += char  # оставляем символы, не являющиеся буквами без изменений
    return result

message = input()

if message != '' and len(message) >= 2 and message[0].isalpha() and message[1].isalpha(): 
    shift = ord(message[0]) + ord(message[1]) - 128
elif message[0].isdigit():
    shift = int(message[0])
else:
    shift = 3

if os.path.exists(message):
    print(f'Файл {message} существует')
    with open(message, 'r') as file:
        text = file.read()
    base64_message = encode_base64(text)
else:
    base64_message = encode_base64(message)
    reversed_base64_message = base64_message[::-1]
    
reversed_base64_message = base64_message[::-1]
middle_index = len(reversed_base64_message) // 2
part1 = reversed_base64_message[:middle_index]
part2 = reversed_base64_message[middle_index:]
swapped_text = part2 + part1
print(caesar_cipher(swapped_text, shift))
    
# decoded_text = decode_base64(base64_message)
# print(decoded_text)
