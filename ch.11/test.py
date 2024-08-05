list = input().split()

list = [(item[1:] + item[0] + "ки") for item in list]

print(*list, sep = " ")

#for i in range(len(list)):
#    item = list[i]
#    swap.append(item[1:]+ item[0])

#swap = [item += "ки" for item in swap]

#for i in range(len(swap)):
#    swap[i] += "ки"
    
#print(*swap, sep = " ") 