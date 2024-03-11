Sequence = 3*'ACGT' + 5*"TTATT"
i = len(Sequence)+1
for i in range(0,i):
    print(Sequence[0:i])
    i = i -1

x = 0
y = 3
for i in range(0,len(Sequence)):
    if len(Sequence[x:y]) == 3:
           print(Sequence[x:y])
    x = x + 1
    y = y + 1
           
    

    
        




