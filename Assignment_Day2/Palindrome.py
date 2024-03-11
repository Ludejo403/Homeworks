def pali(thing):
    b = str(thing)
    if b[::] == b[::-1]:
        return(True)
    else:
        return(False)

             
a = 'Able was I ere I saw elbA'
b = 'madam'
c = 'cat'
d = 90.09
e = 10101

print(pali(a))
print(pali(b))
print(pali(c))
print(pali(d))
print(pali(e))

