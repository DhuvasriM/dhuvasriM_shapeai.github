# -*- coding: utf-8 -*-
"""salting& iteration

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVpZF9GE-dSSHLNhmt7NXhurLWelpyM1
"""

import hashlib
import os

salt = os.urandom(32) 
password = 'ram'

key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000,dklen=128 
)

"""**Storing the Hash and Salt**"""

import os
import hashlib

# Example generation
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', 'mypassword'.encode('utf-8'), salt, 100000)

# Store them as:
storage = salt + key

# Getting the values back out
salt_from_storage = storage[:32] # 32 is the length of the salt
key_from_storage = storage[32:]

"""**Verification**"""

import hashlib

salt = b'' # Get the salt you stored for *this* user
key = b'' # Get this users key calculated

password_to_check = 'krish' # The password provided by the user to check

# Use the exact same setup you used to generate the key, but this time put in the password to check
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'), # Convert the password to bytes
    salt,
    100000
)

if new_key == key:
    print('Password is correct')
else:
    print('Password is incorrect')

"""**Adding Iterations to Hashes**"""

a_dict={'color':'blue','fruit':'apple','pet':'dog'}
for key ,value in a_dict.items():
 print(key,'->',value)