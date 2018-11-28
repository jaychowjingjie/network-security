import hashlib
# b means byte representation of char 'a'
# Note: output of sha1 is 160 bits
h = hashlib.sha1(b'a').hexdigest()
print("The hex digest in base-16 is", h)
print("The integer representation of the hex value above is", int(h,16))
print("The binary is", bin(int(h,16)))
# In conclusion, sha1 sucks...
