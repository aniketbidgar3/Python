def Gen():
    for i in range(1, 5000):
        yield i

# TO Print Numbers as per Requirement


# Roll = Gen()
# print(next(Roll))
# print(next(Roll))
# print(next(Roll))
# print(next(Roll))
# print(next(Roll))


# To print All Numbers in Generators

for i in Gen():
    print(i)
