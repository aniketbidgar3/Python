def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def Partition(arr, l, r):
    p = arr[r]
    i = l-1
    for j in range(l, r+1):
        if (arr[j] < p):
            i += 1
            swap(arr, i, j)

    i += 1
    swap(arr, i, r)
    return i


def QuickSort(arr, l, r):
    if (l < r):
        pi = Partition(arr, l, r)
        QuickSort(arr, l, pi-1)
        QuickSort(arr, pi+1, r)


def arrInput():
    arr = []
    n = int(input("Enter Size : "))
    # print(f"Enter {n} Elements : ", end="")
    for i in range(n):
        a = int(input("Enter : "))
        arr.append(a)
    return arr


arr = arrInput()
print("Unsorted : ", arr)
QuickSort(arr, 0, len(arr)-1)
print("Sorted   : ", arr)
