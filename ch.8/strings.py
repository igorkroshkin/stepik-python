n = int(input())

s = ""

counter = 0

while n > 0:
    if n % 2 == 0:
        s += "0"
    else:
        s += "1"
    n //= 2

for i in range(len(s)-1, -1, -1):
    print(s[i], end="")