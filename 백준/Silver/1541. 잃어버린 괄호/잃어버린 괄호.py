import re


s = input()
numbers = list(map(int, re.findall(r'[+-]?\d+', s)))

result = 0
negative_flag = False
for number in numbers:
    if negative_flag:
        result += -abs(number)
    else:
        if number < 0 :
            negative_flag = True
        result += number
    
print(result)
