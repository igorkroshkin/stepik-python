n = int(input())

list = []

for i in range(n):
    list.append(input())

list2 = []

for i in range(n):
    str = list[i]
    for j in range(len(str)):
        list2.append(str[j])

print(list2)