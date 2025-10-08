#file write example

fh = open ( 'test.txt' , 'w' )
symbols_written=fh. write ( 'hello!' )
print(symbols_written) #6 
fh. close ()

fh = open ( 'test.txt' , 'w+' )
fh. write ( 'hello!' )
fh. seek ( 0 )

first_two_symbols = fh. read ( 5 )
print(first_two_symbols)   # 'he'

fh. close ()

fh = open ( 'test.txt' , 'w' )
fh. write ( 'hello!' )
fh. close ()

fh = open ( 'test.txt' , 'r' )
all_file=fh. read ()
print (all_file) # 'hello!'

fh. close ()



fh = open ( 'test.txt' , 'w' )
fh. write ( 'hello!' )
fh. close ()

fh = open ( 'test.txt' , 'r' )
while True:
    symbol = fh. read ( 1 )
    if  len (symbol) == 0 :
        break 
    print (symbol)

fh. close ()

fh = open ( 'test.txt' , 'w' )
fh. write ( 'first line\nsecond line\nthird line' )
fh. close ()

fh = open ( 'test.txt' , 'r' )
while True:
    line = fh.readline()
    if not line :
        break 
    print ( line )

fh. close ()


fh = open ( 'test.txt' , 'w' )
fh .write ( 'first line\nsecond line\nthird line' )
fh .close ()

fh = open ( 'test.txt' , 'r' )
lines = fh .readlines ()
print (lines)

fh .close ()


fh = open ( "test.txt" , "w" )
fh .write ( "first line\nsecond line\nthird line" )
fh .close ()

fh = open ( "test.txt" , "r" )
lines = [el.strip() for el in fh.readlines()] 
print (lines)

fh .close ()


fh = open ( 'test.txt' , 'w+' )
fh. write ( 'hello!' )

fh. seek ( 1 )
second = fh. read ( 1 )
print( second )   # 'e'

fh. close ()


fh = open( "test.txt" , "w+" )
fh.write( "hello!" )

position = fh.tell()
print ( position ) # 6

fh.seek( 1 )
position = fh.tell()
print ( position ) # 1

fh. read ( 2 )
position = fh.tell()
print ( position ) # 3

fh. close ()