n = int(input())

list = []
chars = []

for i in range(n):
    str = input()
    list.append(str)

k = int(input())

for i in range(n):
    str = list[i]
    if len(str) >= k:
        chars.append(str[k-1])

print(*chars, sep = "")