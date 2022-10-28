# from pwn import xor
# with open("/home/ulmaa/ctf/cryptohack/xor/Lemur_XOR/flag.png",'rb') as f:
#     flag = f.read()


# with open("/home/ulmaa/ctf/cryptohack/xor/Lemur_XOR/lemur.png",'rb') as f:
#     lemur = f.read()

# key = xor(lemur,b'crypto{')

# with open('key.png','wb') as f:
    # f.write(key)

from PIL import Image, ImageChops

im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")
im3 = ImageChops.difference(im1,im2)
im3.save("result.png")