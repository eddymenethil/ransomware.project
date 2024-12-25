import os 
import pyaes

# abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll' # arquivo
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# chave para descriptografa

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover arquivo criptografado
os.remove(file_name)

# criar novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(new_file, 'wb')
new_file.write(decrypt_data)
new_file.close()