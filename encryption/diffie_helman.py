#diffie hellman algorithm

ch='y'



while ch.lower()=='y':
    p=int(input("Enter Value for public key A: "))
    g=int(input("Enter Value for public key B: "))

    a=int(input("Enter Value for private key A: "))
    x=int(pow(g,a,p))
    
    b=int(input("Enter Value for private key B: "))    
    y=int(pow(g,b,p))

    ja=int(pow(y,a,p))
    jb=int(pow(x,b,p))

    print('Secret key for the A is : %d'%(ja))
    print('Secret Key for the B is : %d'%(jb))


    ch=input("Continue (y/n)? ")


