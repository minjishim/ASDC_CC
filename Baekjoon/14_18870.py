# (14주차 : 정렬) 18870 - 좌표 압축

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다. Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다. X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

from sys import stdin

x = int(input())
x_array = list(map(int, input().split()))
# set()을 사용하여 중복 제거, sorted()를 사용하여 배열 정렬
xx_array = sorted(set(x_array))

# dictionary 초기화는 dic = dict() 또는 dic = {}으로 가능
x_dic = {}

# key : value, 즉 여기서 key는 입력값, value는 몇 번째인지를 의미
x_dic = {xx_array[i] : i for i in range(len(xx_array))}

# x_array에 있는 값들을 순차적으로 가져오고, x_array에 있는 것들은 입력 값들임
for i in x_array:
  # 즉, x_dic[입력값(key)]이므로 value를 출력 
  print(x_dic[i], end=' ')

