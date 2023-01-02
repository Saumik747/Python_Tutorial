#AFFINE CIPHER



ch='y'
def emd(s,t):
    x,y, u,v = 0,1, 1,0
    while s != 0:
        q, r = t//s, t%s
        m, n = x-u*q, y-v*q
        t,s, x,y, u,v = s,r, u,v, m,n
    md = t
    return md, x, y
    

def modf(a,m):
    md, x, y = emd(a, m)
    if md != 1:
        return None # modular inverse does not exist
    else:
        return x % m

def a_encrypt(str1,k):
    '''	C = (a*P + b) % 26	'''
    atext=''
    atext=atext+''.join([ chr((( k[0]*(ord(t) - ord('A')) + k[1] ) % 26)+ ord('A')) for t in str1.upper().replace(' ', '') ])
    
    return atext    


def a_decrypt(ctext,k):
    ''' P = (a^-1 * (C - b)) % 26 '''
    dtext=''
    dtext=dtext+''.join([ chr((( modf(k[0], 26)*(ord(c) - ord('A') - k[1]))%  26) + ord('A')) for c in ctext ])
    return dtext


while ch.lower()=='y':
    str1=input("Enter Text: ")
    k=[17,20]
    acet=a_encrypt(str1,k)
    atext=str(acet)
    print('Encrypted Text: {}'.format(acet))
    print('Decrypted Text: {}'.format( a_decrypt(atext, k) ))


    ch=input("Continue for another String(y/n)? ")


         
