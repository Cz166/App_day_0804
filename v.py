def sd():
    list = [2,3,4,5]
    return list

def ss():
    s = sd()
    list_1 = []
    # print(s)
    return [j  for j in s]
    # for i in s:
    #     print(i)
        # list_1.append(i)
        # return list_1

a,b,c,d = ss()
e = ss()
print(a,b,c,d)
h = [i for i in range(len(e))]
try:
    assert 9 in h
except:
    print(5)


