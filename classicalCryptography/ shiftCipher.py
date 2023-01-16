def shift_enc(plain_text, key):
  """
  shift crypto encryption
  """
  plain_text = list(plain_text)
  cipher_text = []
  
  for i in plain_text:
    a = ord(i)
    if a >= 97 and a <= 122:
      cipher_text.append(chr((a - 97 + key) % 26) + 97)
    elif a >= 65 and a <= 90:
      cipher_text.append(chr(((a - 65 + key) % 26) + 65))

    return cipher_text

def shift_dec(cipherText, key):
    """
    shift crypto decryption
    """
    ciphertext = list(cipherText)
    plaintext = []
  
    for i in ciphertext:
        a = ord(i)
        if a >= 97 and a <= 122:
            plaintext.append(chr(((a - 97 - key) % 26) + 97))
        elif a >= 65 and a <= 90:
            plaintext.append(chr(((a - 65 - key) % 26) + 65))
        else :
            plaintext.append(i)

    return plaintext

if __name__ == "__main__":
  # plText = "TMHENQL NBDZM DQZ EQDPTDMS"
    plText = input("please enter a plaintext:\n")
#   print(plText, type(plText))
    print("============result=============")
    for i in range(0,26):
        print("".join(shift_dec(plText, i)))
