def devWord(w):
    arr1 = list(w.upper())
    tmp = []
    arr = []
    for i in range(1, len(arr1)):
        el = arr1[i-1] + arr1[i]
        tmp.append(el)
    for str in tmp:
        if(str.isalpha()):
            arr.append(str)
    return arr

def samePer(arr1, arr2):
    if(arr1 == [] and arr2 ==[]):
        return print(65536)
    if(arr1 == [] or arr2 == []):
        return print(0)
    arr = []
    run = True
    cont = False
    while(run):
        cont = False
        for i in arr1:
            for j in arr2:
                if( i == j ):
                    arr1.remove(i)
                    arr2.remove(j)
                    arr.append(i)
                    cont = True
                    continue
            if(cont):
                continue
        if(not cont):
            run = False
    return print(int((len(arr)/(len(arr)+len(arr1)+len(arr2)))*65536))

samePer(devWord('FRANCE'), devWord('french'))
samePer(devWord('handshake'), devWord('shake hands'))
samePer(devWord('aa1+aa2'), devWord('AAAA12'))
samePer(devWord('E=M*C^2'), devWord('e=m*c^2'))
