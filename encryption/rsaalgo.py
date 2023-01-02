#rsa algorithm
ch='y'
def chkprime(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True


#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                #print("%d = %d*(%d) + %d"%(r,a,e,b))
                pass
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        #print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            #print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
            pass
        elif(s>0):
            #print("s=%d."%(s))
            pass
        return s%r

def rsa_enc(pu_key,ntext):
    e,n=pu_key
    x=[]
    m=0
    j=0
    for i in ntext:
        if(i.isupper()):
            j = ord(i)-65
            c=(j**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x

def rsa_dec(priv_key,c_text):
    d,n=priv_key
    txt=c_text
    x=' '
    m=0
    j=0
    for i in range(len(txt)):
        if(i==400):
            x+=' '
        else:
            m=(int(txt[i])**d)%n
            m+=65
            c=chr(m)
            x+=c  
    return x

    

while ch.lower()=='y':
    
    str1=input("Enter Message: ")
    a=3
    b=11
    a=int(input("Enter Prime number for a: "))
    b=int(input("Enter Prime number for b: "))
    chk_a = chkprime(a)
    chk_b = chkprime(b)
    if(((chk_a==True)or(chk_b==True))):
        n = a * b
        #modulus calculation for rsa
        #print("RSA Modulus(n) is:",n)

        #calculation of euler toitent
        r= (a-1)*(b-1)
        #print("Eulers Toitent(r) is:",r)

        
        for i in range(1,1000):
            if(egcd(i,r)==1):
                e=i
        #print("The value of e is:",e)

        #calculation of private and public key
        #print("EUCLID'S ALGORITHM:")
        eugcd(e,r)
        #print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
        #print("*****************************************************")
        #print("EUCLID'S EXTENDED ALGORITHM:")
        d = mult_inv(e,r)
        #print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
        #print("The value of d is:",d)
        #print("*****************************************************")
        public = (e,n)
        private = (d,n)
        print("Private Key is:",private)
        print("Public Key is:",public)

        enc_msg=rsa_enc(public,str1)
        dec_msg=rsa_dec(private,enc_msg)
        print("Your encrypted message is:",enc_msg)
        print("Decrypted text of above encryption is :",dec_msg)      

    else:
        print("enterd value is not prime number try again")
       
        
  
   
    ch=input("Continue for another String(y/n)?: ")
