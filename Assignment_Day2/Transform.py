def transform(lists):
    t = 0
    for i in lists:
        if i >= 0:
            i = "a"
            t =+ 1
        return(t != 0)

a = [1,3, -2, 5, 3, 7. -1, 1.05, -1.3]
b = [-1,-2,-4]
print(transform(a))
print(transform(b))

        
