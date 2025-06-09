# hello.py

import base64
import os

# Vulnerabilidade 1. Command Injection (Injeção de Comando)
# Vulnerabilidade: Ocorre quando a entrada do usuário é usada diretamente 
# em comandos executados no shell do sistema operacional, permitindo que um
#  atacante execute comandos arbitrários no servidor.
def ping_host_vulnerable(host):
    # !!! VULNERÁVEL: Concatenação direta da entrada do usuário em um comando shell
    command = f"ping -c 1 {host}"
    print(f"Executando comando: {command}")
    os.system(command) # ou subprocess.run(command, shell=True)

# Vulnerabilidade 2. Password HardCode
username = "jean"
password = "abc@123"

# Combine username and password
credentials = f"{username}:{password}"

# Encode to base64
encoded_credentials = base64.b64encode(credentials.encode()).decode()

print("Meu primeiro codigo Python + GitHub Action!")
print("Authorization: Basic amVhbjphYmNAMTIz")
print("\033[42mVersao Verde\033[0m")
print(f"Decode {credentials} | Encoded {encoded_credentials}") 
