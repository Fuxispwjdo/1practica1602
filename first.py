arr = list()
l = int(input("Enter number of elements: "))
print("Enter elements:")
i = 0
while (i < l):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
while (i < l):
    print(arr[i], end = " ")
    i += 1
print("")
