s = input()

h1 = s.find("h")
h2 = s.rfind("h")

s3 = s[:h1+1]
s4 = s[h1+1:h2]
s4 = s4[::-1]
s5 = s[h2:]

print(s3, s4, s5, sep = "")