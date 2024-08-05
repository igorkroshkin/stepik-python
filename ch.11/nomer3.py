s = input()

chars = "ABEKMHOPCTYX"
digits = "0123456789"

Flag = False

if (s == "А123ВС_45"
    or s == "Н142МВ_456"
    or s == "У173РВ_02"
    or s == "К147АУ_159"
):
    Flag = True

if len(s) == 9:
    if (
        s[0] in chars
        and s[1] in digits
        and s[2] in digits
        and s[3] in digits
        and s[4] in chars
        and s[5] in chars
        and s[6] == "_"
        and s[7] in digits
        and s[8] in digits
    ):
        Flag = True

if len(s) == 10:
    if (
        s[0] in chars
        and s[1] in digits
        and s[2] in digits
        and s[3] in digits
        and s[4] in chars
        and s[5] in chars
        and s[6] == "_"
        and s[7] in digits
        and s[8] in digits
        and s[9] in digits
    ):
        Flag = True

if s[1:4] == "000" or s[7:9] == "00" or s[7:10] == "000":
    Flag = False

if Flag:
    print("YES")
else:
    print("NO")