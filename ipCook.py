def sum(arr):
    ans = 0
    for i in arr:
        ans += i
    return ans

def max(arr):
    ans = 0
    for i in arr:
        if(ans < i):
            ans = i
    return ans

def min(arr):
    ans = 9999999
    for i in arr:
        if(i < ans):
            ans = i
    return ans

def minNextNum(arr, tmp):
    arr1 = []
    for i in range(len(arr)):
        arr1.append(int(tmp[i]*(arr[i]/tmp[i] + 1)))
    return min(arr1)

def nextNum_int(n1, n2):
    return int(n2*(n1/n2 + 1))

def ipCook(n, arr):
    tmp = []
    cnt = 2
    for i in arr:
        tmp.append(i)
    for i in range(n+1):
        a = minNextNum(arr, tmp)
        for j in range(0, len(arr)):
            if(nextNum_int(arr[j], tmp[j]) == a):
                arr[j] = int(tmp[j]*(arr[j]/tmp[j] + 1))
                cnt += 1
        if(n <= cnt):
            return print(max(arr))

ipCook(6, [7,10])

ipCook(10, [1,4,5])