#!/usr/bin/env python


import os

## get_random_bytes
## Read file /dev/urandom and return bytes value
def get_random_bytes(num_bytes):
    with open('/dev/urandom', 'rb') as f: # Read and Binary
        return f.read(num_bytes) # Read arg, the number of bytes to return 

random_bytes_1 = get_random_bytes(8) # return byte number
print(random_bytes_1.hex()) # convert byte to hex


# Using os function()
random_bytes_2 = os.urandom(1)  # get 4 random bytes
print(int.from_bytes(random_bytes_2, byteorder='big'))  # convert bytes to integer in big indian, byteorder='little' if use little indian
