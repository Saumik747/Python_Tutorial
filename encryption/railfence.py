ch='y'
def railenc(str1,k):
    rail = [['\n' for i in range(len(str1))] for j in range(k)]
    # to find the direction
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(str1)):
            
            # checking direction flow
            # reverse the direction if we've just
            # filled the top or bottom rail
            if (row == 0) or (row == k - 1):
                    dir_down = not dir_down
            
            # fill the corresponding alphabet
            rail[row][col] = str1[i]
            col += 1
            
            # find the next row using
            # direction flag
            if dir_down:
                    row += 1
            else:
                    row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(k):
            for j in range(len(str1)):
                    if rail[i][j] != '\n':
                            result.append(rail[i][j])
    return("" . join(result))


def raildec(cipher, key):

	# create the matrix to cipher
	# plain text key = rows ,
	# length(text) = columns
	# filling the rail matrix to
	# distinguish filled spaces
	# from blank ones
	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	
	# to find the direction
	dir_down = None
	row, col = 0, 0
	
	# mark the places with '*'
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		
		# place the marker
		rail[row][col] = '*'
		col += 1
		
		# finding the next row
		# using direction flag
		if dir_down:
			row += 1
		else:
			row -= 1
			
	# now we can construct the
	# fill the rail matrix
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	# now read the matrix in
	# zig-zag manner to construct
	# the resultant text
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		
		# check the direction of flow
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
			
		# place the marker
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		# find the next row using
		# direction flag
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

    


while ch.lower()=='y':
    print("Railfence cipher ")
    str1=input("Enter Text: ")
    k=int(input("Enter Key value (2,3,4): "))
    lst=[2,3,4]
    enc=railenc(str1,k)
    if(k in lst):
        if(len(str1)==k):
            print("please enter key value greater than no of characters")
        else:
            print("Encrypted text: ",railenc(str1,k))
            print("Decrypted Text: ",raildec(enc,k))
    else:
        print("key value out of range")

        


    ch=input("COntinue for another String(y/n)?")

