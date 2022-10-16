# (12주차 : 정렬) 7453 - 합이 0인 네 정수

# 정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다. A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

from sys import stdin

input = stdin.readline

n = int(input())

a_list, b_list, c_list, d_list = [], [], [], []
ab_dic = dict()
result = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

for a in a_list:
    for b in b_list:
        ab = a + b
        if ab not in ab_dic.keys():
            # keys : ab, value : 1
            ab_dic[ab] = 1
        else:
            ab_dic[ab] += 1

for c in c_list:
    for d in d_list:
        # ab + cd = 0, 이 경우에 ab = -(cd)
        cd = (-1) * (c + d)
        if cd in ab_dic.keys():
            result += ab_dic[cd]

print(result)