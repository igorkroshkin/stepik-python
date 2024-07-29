n1, n2 = int(input()), int(input())

if n1 == 1:
    n1 += 1

for i in range(n1, n2 + 1):
    if_simple = 1
    for j in range(2, i):
        if i % j == 0:
            if_simple = 0
    if if_simple == 1:
        print(i)