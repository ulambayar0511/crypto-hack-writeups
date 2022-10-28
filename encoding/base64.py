# Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters. One character of a Base64 string encodes 6 bits, and so 4 characters of Base64 encode three 8-bit bytes.
# Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.
import base64
flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b = bytes.fromhex(flag)
print(base64.b64encode(b))