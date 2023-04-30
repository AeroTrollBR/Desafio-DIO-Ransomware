from cryptography.fernet import Fernet

with open('TCC.txt','rb') as f:
	conteudo = f.read()

chave = Fernet.generate_key()

fernet = Fernet(chave)

conteudo_criptografado = fernet.encrypt(conteudo)

with open('arquivo_criptografado.txt','wb') as f:
	f.write(conteudo_criptografado)

with open('chave.key','wb') as f:
	f.write(chave)
