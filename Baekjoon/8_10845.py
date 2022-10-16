# (8주차 : 큐) 큐

import sys  # sys.stdin.readline() 사용
from collections import deque  # deque 사용

data = deque([])
answer = list()
n = int(input())  # n : 명령의 수

for n_index in range(n):
    # order = list(input().split()) => 반복문 사용 시 input()은 시간초과가 발생할 수 있음. sys.stdin.readline()를 사용해야 함.
    order = list(sys.stdin.readline().split())

    if (order[0] == 'push'):
        data.appendleft(order[1])

    elif (order[0] == 'pop'):
        # is not None 또는 != None으로 사용함(!= null의 의미)
        # if 구문의 경우 그냥 아래처럼 사용 가능
        if data:
            # 인덱스를 지정하지 않을 경우 pop은 해당 리스트의 마지막 항목을 삭제하고 돌려주기 때문에, print(data.pop())을 할 경우 data.pop()에서 pop이 1회 실행된 후에 해당 pop된 값을 print안의 value로 돌려줌
            print(data.pop())
            # data.pop()
        else:
            print('-1')

    elif (order[0] == 'size'):
        print(len(data))

    elif (order[0] == 'empty'):
        if data:
            print('0')
        else:
            print('1')

    elif (order[0] == 'front'):
        if data:
            print(data[-1])
        else:
            print('-1')

    elif (order[0] == 'back'):
        if data:
            print(data[0])
        else:
            print('-1')
