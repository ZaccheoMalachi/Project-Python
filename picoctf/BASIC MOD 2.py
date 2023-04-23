def mod_inverse(a, m):
    """
    Returns the modular inverse of a mod m.
    If the modular inverse doesn't exist, returns None.
    """
    def extended_gcd(aa, bb):
        last_remainder, remainder = abs(aa), abs(bb)
        x, last_x, y, last_y = 0, 1, 1, 0
        while remainder:
            last_remainder, (quotient, remainder) = remainder, divmod(last_remainder, remainder)
            x, last_x = last_x - quotient*x, x
            y, last_y = last_y - quotient*y, y
        return last_remainder, last_x * (-1 if aa < 0 else 1), last_y * (-1 if bb < 0 else 1)
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    return x % m
character=[]
for i in range(26):
    character.append(chr(97+i))
for i in range(10):
    character.append(chr(48+i))
character.append('_')
list=[104,372,110,436,262,173,354,393,351,297,241,86,262,359,256,441,124,154,165,165,219,288,42]
for i in list:
    print(character[mod_inverse(i,41)-1])
