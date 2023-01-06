import string
secret='lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
# print(ALPHABET[6])
# print(ALPHABET[9])
def b16_decode(enc):
    plain=''
    for i in secret:
        bin="{0:04b}".format(ALPHABET.index(i))
        print(bin)
b16_decode(secret)