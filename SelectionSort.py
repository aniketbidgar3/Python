arr = [3, 5, 2, 7, 1]

print(arr)

n = len(arr)

for i in range(0, n-1):
    for j in range(i+1, n):
        if (arr[j] < arr[i]):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp


# same as above but by finding Minimum element every time

# for i in range (0,n-1):
#     min=arr[i]
#     for j in range (i+1,n):
#        if(arr[j]<min):
#         temp=min
#         min=arr[j]
#         arr[j]=temp
#     arr[i]=min


print(arr)
