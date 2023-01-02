#caesar cipher encryption and decryption
ch='y'

def enc(str1,k):
    print("Encrypting text")
    ctext=""
    for i in range(len(str1)):
        char = str1[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            ctext += chr((ord(char) + k-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            ctext += chr((ord(char) + k - 97) % 26 + 97)
    return ctext

def dec(str1,k):
    print("Decrypting text")
    ptext=""
    for i in range(len(str1)):
        char = str1[i]
        if (char.isupper()):
            ptext += chr((ord(char) - k-65) % 26 + 65)
        else:
            ptext += chr((ord(char) - k - 97) % 26 + 97)
    return ptext

    



    
while ch.lower()=='y':
    str1=input("Enter Text: ")
    k=int(input("Enter key value in number: "))
    s=enc(str1,k)
    #print("Select Option\n1.Encryption \n2.Decryption")
    n=int(input("Enter choice: "))

    print(enc(str1,k))
    print(dec(s,k))
        
    ch=input("continue for another String (y/n)?")
    
