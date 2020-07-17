import pyaes
key = 'ds,dfh/khsiaj94i*&%vfker/{27&^$#@Xx#b0)'
message = 'hello there,how you doing?'
cipher = pyaes.AESModeOfOperationOFB(key)
key = key.encode('utf-8')
def pad(s):
    return s +((16-len(s) % 16) * '{')

def encrypt(plaintext):
    global cipher
    return cipher.encrypt(pad(plaintext))

def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt(ciphertext).decode('utf-8')
    l = dec.count('{')
    return dec[:len(dec)-1]

print('Message :',message)
encrypted = encrypt(message)
decrypted = decrypt(encrypted)
print("Encryted :", encrypted)
print("decrpted :",decrypted)
