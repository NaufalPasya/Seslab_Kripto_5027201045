data = "label"
xor = ''

for c in data:
    xor += chr(ord(c) ^ 13)

print('crypto{{{}}}'.format(xor))