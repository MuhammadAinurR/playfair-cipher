import playfair_cipher_encrypt as en
import playfair_cipher_decrypt as dc

key_text = "Velocity"

plain_text = "garuda"

print("Key :", key_text)
print("Text :", plain_text)
decrypted_message = en.final(key_text, plain_text)
print("Encrypt :", decrypted_message)
print("Decrypted :", dc.final(key_text, decrypted_message))
