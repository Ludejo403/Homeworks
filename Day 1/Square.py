x = 0
Squares = {}

while x**2 <= 100:
    s = str(x)
    q = x**2
    Squares.update({s:q})
    x = x + 1
    print(f"{q} is the square of {s}")

    

