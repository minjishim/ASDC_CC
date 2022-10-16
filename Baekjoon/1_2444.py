# (1주차) 별 찍기 - 7

i = 0
num = int(input())
inStr = []

for i in range(0, num, 1):
    inStr.append((' ' * (num - i - 1)) + ('*' * ((2 * i) + 1)))
    print(inStr[i])

for i in range(1, num, 1):
    print(inStr[num - i - 1])
