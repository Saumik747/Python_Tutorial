#vernam cipher
# both input and output must be same length and alpha-numeric

def vernam_enc(ptext,key):

    # convert into lower cases and remove spaces
    
    ptext=ptext.replace(" ","")
    key=key.replace(" ","")
    ptext=ptext.lower()
    key=key.lower()
    
    # conditional statements
    if(len(ptext)!=len(key)):
        print("Lengths are different")
        
        
    else:
        ctext=""
        
        # iterating through the length
        for i in range(len(ptext)):
            k1=ord(ptext[i])-97
            k2=ord(key[i])-97
            s=chr((k1+k2)%26+97)
            ctext+=s
        print("Enrypted message is: ",ctext)
        return ctext
        
def vernam_dec(ctext,key):

    # convert into lower cases and remove spaces
    ctext=ctext.lower()
    key=key.lower()
    ctext=ctext.replace(" ","")
    key=key.replace(" ","")
    
    ptext=""
    
    # iterating through the length
    for i in range(len(ctext)):
        k1=ord(ctext[i])-97
        k2=ord(key[i])-97
        s=chr((((k1-k2)+26)%26)+97)
        ptext+=s
    print("Decrypted message is: ",ptext)
    return ptext


ch='y'

while ch.lower()=='y':
    
    ptext=input("Enter the message: ")
    key=input("Enter the one time pad: ")
    vec=vernam_enc(ptext,key)
    vedc=vernam_dec(vec,key)
    ch=input("continue for another String(y/n)? ")

