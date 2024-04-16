import numpy as np

def countingSort(a):
    k = max(map(lambda p: p[0], a))
    # Or: max(a)[0]
    b = np.array(a)
    c = np.array([0]*(k + 1))
    
    for (x,i) in a:
        c[x] += 1
    
    for i in range(1, k + 1):
        c[i] = c[i] + c[i - 1]
        
    for i in range(len(a), 0, -1):
        b[c[a[i - 1][0]] - 1] = a[i - 1]
        c[a[i - 1][0]] = c[a[i - 1][0]] - 1
    
    return b

def _radixSort(a):
    n = len(a) # Number of integers to be sorted
    d = len(a[0]) # Number of digits in each integer
    b = np.array(a)
    
    for t in range(d - 1, -1, -1):
        c = np.array([0]*10)
        for i in range(n):
            c[a[i][t]] += 1
        
        for i in range(1, 10):
            c[i] = c[i] + c[i - 1]
        
        for i in range(n, 0, -1):
            b[c[a[i - 1][t]] - 1] = a[i - 1]
            c[a[i - 1][t]] = c[a[i - 1][t]] - 1
        a = np.array(b)
            
    return map(list, b)

def intToDigits(n):
    if n < 10:
        return [n]
    else:
        return intToDigits(n//10) + [n%10]
    
def digitsToInt(ds):
    if ds == []:
        return 0
    else:
        return ds[-1] + 10*digitsToInt(ds[:-1])
    
def homogenise(a):
    d = max(map(len, a))
    return list(map(lambda ds: (d - len(ds))*[0] + ds, a))

def listMap(f, xs):
    return list(map(f, xs))

def radixSort(a):
    return listMap(digitsToInt, _radixSort(homogenise(listMap(intToDigits, a))))







