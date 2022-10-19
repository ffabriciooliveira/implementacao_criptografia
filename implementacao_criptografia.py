

from cryptography.fernet import Fernet #IMPORTA MÓDULO pip install cryptography  

 

# OBTEM A MENSAGEM  

mensagemOriginal = ("Testando criptografia")  

 

# GERA UMA CHAVE ALEATÓRIA DE CRIPTOGRAFIA E A EXIBE  

chave = Fernet.generate_key()  

fernet = Fernet(chave) # PREPARA A CHAVE PARA O USO  

 

# CRIPTOGRAFA  

mensagemCriptografada = fernet.encrypt(mensagemOriginal.encode())  

 

# DESCRIPTOGRAFA  

mensagemDescriptograda = fernet.decrypt(mensagemCriptografada).decode()  

 
 

print ("A mensagem original é: "+mensagemOriginal)  

print ("A chave de criptografia e:",chave)  

print ("A mensagem criptografada é: ",mensagemCriptografada)  

print ("A mensagem descriptograda é: "+mensagemDescriptograda)

