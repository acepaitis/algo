import math

def merge(arr, start, middle, end):
    nLeft = middle - start + 1
    nRight = end - middle

    leftArr = list(range(nLeft + 1))
    rightArr = list(range(nRight + 1))
    for iLeft in range(0, nLeft):
        leftArr[iLeft] = arr[start + iLeft]
    for iRight in range(0, nRight):
        rightArr[iRight] = arr[middle + iRight + 1]

    leftArr[nLeft] = float('inf')
    rightArr[nRight] = float('inf')

    iLeft = 0
    iRight = 0

    for iAll in range(start, end + 1):
        if(leftArr[iLeft] <= rightArr[iRight]):
            arr[iAll] = leftArr[iLeft]
            iLeft = iLeft + 1
        else:
            arr[iAll] = rightArr[iRight]
            iRight = iRight + 1


        

def mergeSort(arr, startIndex, endIndex):
    if arr is None:
        raise ValueError('arr is none')
    if len(arr) < 2:
        return
    if startIndex < 0 or endIndex < 0:
        raise Exception('startIndex and endIndex indices must be more than 0')
    if startIndex < endIndex:
        midIndex = (startIndex + endIndex) // 2
        mergeSort(arr, startIndex, midIndex)
        mergeSort(arr, midIndex + 1, endIndex)
        merge(arr, startIndex, midIndex, endIndex)
    
arr = [56, 5, 1, 9, 3, 10, 2, 9, 7]

mergeSort(arr, 0, len(arr) - 1)

for item in arr:
    print(str(item) + ', ')