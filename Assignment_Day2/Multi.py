def multi(numbers):
    m=1
    for i in numbers:
        if i >= 0:
            m = m*i

    return(m)

a = [1,2,4,-1,3, -5, 1.04]
print(multi(a))
            
