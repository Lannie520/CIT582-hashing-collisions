import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    table = {}

    while True:
        x = os.urandom(64)
        # Bin turns strings to bytes
        hash = bin(int(hashlib.sha256(x).hexdigest(), 16))[-k:]
        if hash in table:
            if x == table[hash]:
                continue
            else:
                y = table[hash]
                #print(hash)
                return(x, y)
        else:
            table[hash] = x
#Test the result
print(hash_collision(16))




