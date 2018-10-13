import binascii
import base64

str_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
str_out = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

x = base64.b64encode(binascii.unhexlify(str_in))
x = x.decode("utf-8") 
print(x == str_out)
