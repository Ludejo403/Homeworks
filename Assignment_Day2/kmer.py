Sequence = 3*'ACGT' + 5*"TTATT"



def kmer(Sequence,k):
    x = 0
    y = k
    kmeri={}
    for i in range(0,len(Sequence)):
        if len(Sequence[x:y]) == k:
            kmeri.update({str(x+1):Sequence[x:y]})
        x = x + 1
        y = y + 1
    print(kmeri)

kmer(Sequence,37)
