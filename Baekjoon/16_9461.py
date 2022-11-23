# (16주차 : 다이나믹 프로그래밍) 9461 - 파도반 수열

# 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다. 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다. N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

from sys import stdin

input = stdin.readline

t = int(input())
answer = [0] * t
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
pp = [0] * 91
i = 0

def pn(nn):
  for i in range(10, nn + 1, 1):
    p[i] = p[i - 2] + p[i - 3]

for i in range(0, t, 1):
  n = int(input())
  if (n < 11):
    answer[i] = p[n - 1]
  else:
    p.extend(pp)
    pn(n - 1)
    answer[i] = p[n - 1]

for i in answer:
  print(i)
