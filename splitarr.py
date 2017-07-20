def checkSum(arr):
    wR = 0
    total = arr[0]

    while(wR < len(arr)):
        if total < sum(arr[wR+1:]):
            wR += 1
            total +=arr[wR]
        if total == sum(arr[wR+1:]):
            return arr[:wR+1],arr[wR+1:]
        if total > sum(arr[wR+1:]):
            return False
    return False

'''def checkSum(arr):
    wR=0
    total = arr[0]
    while(wR<len(arr)):
        if total<sum(arr[wR+1:]):
            wR +=1
            total += arr[wR]
        if total==sum(arr[wR+1:]):
            return arr[:wR+1],arr[wR+1:]
        if total>sum(arr[wR+1:]):
            return False
    return False'''



arr=[[1,2,3,3,2,1],[1,2,3,4,5,6,21],[1,90, 50, 30, 5, 3, 2, 1 ],[1, 50, 900, 1000 ]]
for test in arr:
    print checkSum(test)