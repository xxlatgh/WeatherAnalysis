# discussion on list and dict comprehension
lst = []
d={}
for n, l in zip(range(10), string.lowercase[:10]):
    lst.append(""{}{}"".format(n, l))
    d[n]=l
d={n:l for n,l in zip(range(10), string.lowercase[:10])}
