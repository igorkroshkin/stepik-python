def is_valid_password(password):
    num1 = int(password[0:password.find(":")])
    num = password[password.find(":") + 1:]
    num2 = int(num[0:num.find(":")])
    num3 = num[num.find(":") + 1:]
    
    if str(num1) == str(num1)[::-1]:
        flag_1 = True
    else:
        flag_1 = False

    for i in range(2, num2):
        if num2 % i == 0:
            flag_2 = False
            break
        else:
            flag_2 = True

    if num3.isdigit() and int(num3) % 2 == 0:
        flag_3 = True
    else:
        flag_3 = False

    if flag_1 and flag_2 and flag_3:
        return True
    else:
        return False

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22'))