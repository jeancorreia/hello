# hello.py

import base64

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
