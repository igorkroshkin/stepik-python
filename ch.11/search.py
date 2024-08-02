num1 = int(input())

list1 = []

for i in range(num1):
    list1.append(input())

num2 = int(input())

list2 = []

for i in range(num2):
    list2.append(input())

list3 = []

for i in range(len(list1)):
    counter = 0
    for j in range(len(list2)):
        if list2[j].lower() in list1[i].lower():
            counter += 1
    if counter == len(list2):
        list3.append(list1[i])

print(*list3, sep = "\n")