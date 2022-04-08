import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

a = requests.get(f"{BASE_URL}/encrypt_flag")
data = a.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

a = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = a.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

print("flag", bytearray.fromhex(plaintext).decode())