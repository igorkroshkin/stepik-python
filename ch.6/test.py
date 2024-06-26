num = int(input())

f1 = 0
f2 = 1

print(f2, end = " ")
for _ in range(num-1):
    f1, f2 = f2, f1+ f2
    print(f2, end = " ")