n = 5


# # Square
# for i in range(n):
#     for j in range(n):
#         print(" *",end=" ")
#     print()


# # Left Aligned Triangle
# for i in range(n):
#     for j in range(i+1):
#         print(" *",end=" ")
#     print()


# # Right Aligned Triangle
# for i in range(n):
#     for j in range(n-1-i,0,-1):
#         print("  ",end=" ")
#     for j in range(i+1):
#         print(" *",end=" ")
#     print()


# # Equilateral Triangle
# for i in range(n):
#     for j in range(n-1-i,0,-1):
#         print("  ",end=" ")
#     for j in range(2*i+1):
#         print(" *",end=" ")
#     print()


# # Kite
# for i in range(n):
#     for j in range(n-1-i,0,-1):
#         print("  ",end=" ")
#     for j in range(2*i+1):
#         print(" *",end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-1-i,0,-1):
#         print("  ",end=" ")
#     for j in range(2*i+1):
#         print(" *",end=" ")
#     print()


# # Diamond
# for i in range(n):
#     for j in range(n-1-i,0,-1):
#         print("  ",end="")
#     for j in range(2*i+1):
#         print(" *",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-1-i,0,-1):
#         print("  ",end="")
#     for j in range(2*i+1):
#         print(" *",end="")
#     print()


# Hollow Diamond
for i in range(n):
    for j in range(n-1-i, 0, -1):
        print("  ", end="")
    for j in range(2*i+1):
        if (j == 0 or j == 2*i):
            print(" *", end="")
        else:
            print("  ", end="")

    print()
for i in range(n-2, -1, -1):
    for j in range(n-1-i, 0, -1):
        print("  ", end="")
    for j in range(2*i+1):
        if (j == 0 or j == 2*i):
            print(" *", end="")
        else:
            print("  ", end="")
    print()
