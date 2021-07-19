def InsertionSort(listToSort):
    for outerIndex in range(1, len(listToSort)):
        key = listToSort[outerIndex]
        innerIndex = outerIndex - 1
        while innerIndex > -1 and listToSort[innerIndex] > key:
            listToSort[innerIndex + 1] = listToSort[innerIndex]
            innerIndex = innerIndex - 1
        listToSort[innerIndex + 1] = key

arr = [56, 5, 1, 9, 3, 10, 2, 9, 7]

InsertionSort(arr)

for item in arr:
    print(str(item) + ',')
