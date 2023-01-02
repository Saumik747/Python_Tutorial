#Vignere cipher mapping in row column format of alphabets is done
ch='y'
def keygen(str1,k):
    k=list(k)
    ktext=''
    if len(str1)==len(k):
        return k
    else:
        for i in range(0,len(str1)-len(k)):
            k.append(k[i % len(k)])
        ktext+=ktext.join(k)
        return ktext

def vinc(str1,k):
    ctext=[]
    dtext=''
    for i in range(0,len(str1)):
        a=(ord(str1[i])+ord(k[i])) % 26
        a+=ord('A')
        ctext.append(chr(a))
    dtext+=dtext.join(ctext)
    return dtext

def videc(vitext,k):
    vtext=[]
    vetext=''
    for i in range(0,len(vitext)):
        b=(ord(vitext[i])-ord(k[i])+26)%26     
        b+=ord('A')
        vtext.append(chr(b))
    vetext+=vetext.join(vtext)
    return vetext

while ch.lower()=='y':
    str1=input("Enter Your String: ")
    k=input("Enter your Keyword: ")
    if(str1.isalpha() and k.isalpha()):
        #print(True)
        k1=keygen(str1.upper(),k.upper())
        a=vinc(str1.upper(),k1)
        b=videc(a.upper(),k1)
        print("Entered text: ",str1.upper(),"\nEntered Keyword: ",k.upper())
        print("Encrypted Text: ",a)
        print("Decrypted Text: ",b)
        
    else:
        print("Please Enter Only alphabets")
   
    ch=input("Continue for another String (y/n)? ")
