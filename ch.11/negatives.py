n = int(input())

list = []
list2 = []

for i in range(n):
    num = int(input())
    list.append(num)

for i in range(0, n, 2):
    list2.append(list[i])

print(list2)