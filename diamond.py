rows = int ( input ("Enter a number of rows: "))
character  = "* "
for i in range ( 1, rows +1 ):  #Creating a for loop to print the top half of the palindrome
    print ( " " * ( rows - i ) + character * ( i ) )
    
for j in range( rows-1, 0, -1 ): #Creating another for loop to print the bottom half of the palindrome
     print ( " " * ( rows - j ) + character * ( j ) )
    
