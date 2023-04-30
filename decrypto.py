import sys
from cryptography.fernet import Fernet

with open('arquivo_criptografado.txt', 'rb') as f:
	conteudo_criptografado = f.read()

with open('chave.key', 'rb') as f:
	chave = f.read()

fernet = Fernet(chave)

conteudo_descriptografado = fernet.decrypt(conteudo_criptografado)

with open('meu_arquivo_descriptografado.txt', 'wb') as f:
	f.write(conteudo_descriptografado)
