def Merge(arr, l, mid, r):
    n1 = mid-l+1
    n2 = r-mid

    a = []
    b = []

    for i in range(n1):
        a.append(arr[l+i])

    for i in range(n2):
        b.append(arr[mid+i+1])

    i = j = 0
    k = l

    while (i < n1 and j < n2):
        if (a[i] < b[j]):
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1

    while (i < n1):
        arr[k] = a[i]
        i += 1
        k += 1

    while (j < n2):
        arr[k] = b[j]
        j += 1
        k += 1


def MergeSort(arr, l, r):
    if (l < r):
        mid = (l+r)//2
        MergeSort(arr, l, mid)
        MergeSort(arr, mid+1, r)
        Merge(arr, l, mid, r)


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
MergeSort(arr, 0, len(arr)-1)
print("Sorted   : ", arr)
