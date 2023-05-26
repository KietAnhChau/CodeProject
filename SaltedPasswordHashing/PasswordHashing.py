#!/usr/bin/env python

import hashlib
import secrets

hash_object = hashlib.sha512() # Create a hash object by calling the sha512() constructor method

# generate salt token
# token_bytes, Return a random byte string containing nbytes number of bytes.
# token_hex, Return a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits.
# token_urlsafe, Return a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.

salt = secrets.token_bytes(8) # 8 random bytes
print(salt)

data = b'P@ssW0rd'
salted_data = salt + data

hash_object.update(salted_data) # Feed the hash object with the bytes-like objects (normally bytes) using the update() method

# Get the digest of the concatenation of the data fed to the object so far using the digest() or hexdigest() method
hashed_string = hash_object.hexdigest()

print(hashed_string)