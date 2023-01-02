#playfair
# Create a 5x5 matrix using a secret key
"""
def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    # add the key to the matrix
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    #Add the rest of the alphabet to the matrix
    # A=65 ... Z=90
    for letter in range(65,91):
        if letter==74: # I/J are in the same position
                continue
        if chr(letter) not in letters_added: # Do not add repeated letters
            letters_added.append(chr(letter))
            
    #print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix
#Return the index of a letter in the matrix
#This will be used to know what rule (1-4) to apply
def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue



def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message


#Implementation of the playfair cipher
#If encrypt=True the method will encrypt the message
# otherwise the method will decrypt
def playfair(key, message, encrypt=True):
    inc = 1
    if encrypt==False:
        inc = -1
    matrix = create_matrix(key)
    message = message.upper()
    message = message.replace(' ','')    
    message = separate_same_letters(message)
    cipher_text=''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: #Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:# Rule 3, the letters are in the same column
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: #Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

if __name__=='__main__':
    # a sample of encryption and decryption
    print ('Encripting')
    print ( playfair('secret', 'my secret message'))
    print ('Decrypting')
    print ( playfair('secret', 'LZECRTCSITCVAHBT', False))
"""

ch='y'
def crt_matrix(s):
    k=s.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    for letter in k:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
            
    #Add the rest of the alphabet to the matrix
    # A=65 ... Z=90
    for letter in range(65,91):
        if letter==74: # I/J are in the same position
                continue
        if chr(letter) not in letters_added: # Do not add repeated letters
            letters_added.append(chr(letter))
            
    #print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix

def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue
    

def sep_same_letter(msg):
    index = 0
    while (index<len(msg)):
        l1 = msg[index]
        if index == len(msg)-1:
            msg = msg + 'X'
            index += 2
            continue
        l2 = msg[index+1]
        if l1==l2:
            msg = msg[:index+1] + "X" + msg[index+1:]
        index +=2   
    return msg



def dec_enc(str1,s,doenc):
    inc=1
    if doenc==False:
        inc=-1
    matrix=crt_matrix(s)
    msg=str1.upper()
    msg=msg.replace(' ','')
    msg=sep_same_letter(msg)
    ctext=''
    for (l1, l2) in zip(msg[0::2], msg[1::2]):
        #
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: #Rule 2, the letters are in the same row
            ctext += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:# Rule 3, the letters are in the same column
            ctext += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: #Rule 4, the letters are in a different row and column
            ctext += matrix[row1][col2] + matrix[row2][col1]
    
    return ctext

    
    


while ch.lower()=='y':
    str1=input("Enter String: ")
    s=input("Enter Keyword: ")
    playenc=dec_enc(str1,s,True)
    print("Encrrypted Text: ",playenc)
    playdec=dec_enc(playenc,s,False)
    print("Decrrypted Text: ",playdec)

    ch=input("continue (y/n)? ")




