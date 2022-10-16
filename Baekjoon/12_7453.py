# (12주차 정렬+이진탐색) 합이 0인 네 정수
from sys import stdin

#빠른 입출력
input = stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
AB = dict()
result = 0

for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)


for a in A:
  for b in B:
    ab = a + b
    # ab가 key로 없다면, value를 1로 저장
    if ab not in AB.keys():
      AB[ab] = 1
    # ab가 key로 존재한다면, value를 +1 해서 저장
    else:
      AB[ab] += 1

for c in C:
  for d in D:
    cd = (-1) * (c + d)
    if cd in AB.keys():
      result += AB[cd]

print(result)