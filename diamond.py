rows = int ( input ("Enter a number of rows: "))
character  = "* "
for i in range ( 1, rows +1 ):
    print ( " " * ( rows - i ) + character * ( i ) )
    
for j in range( rows-1, 0, -1):
     print ( " " * ( rows - j ) + character * ( j ) )
    