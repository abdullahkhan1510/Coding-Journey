def decrypt(ciphertext, key):
    word = ""
    for i in range (len(ciphertext)):
        word = word + chr(ciphertext[i]^key)
    return(word)
ciphertext = [8, 14, 12, 7, 29, 115, 105, 4, 12, 12, 29, 105, 8, 29, 105, 4, 0, 13, 7, 0, 14, 1, 29]
key = 0
decrypt(ciphertext, key)

while key < 256:
    if (decrypt(ciphertext, key))[:7] == "AGENT: ":
        print(decrypt(ciphertext, key))
        print(key)
        break
    else:
        key = key + 1
