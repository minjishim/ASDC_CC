# (17주차 : 다이나믹 프로그래밍) 2579 - 계단 오르기

# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다. 계단 오르는 데는 다음과 같은 규칙이 있다.
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다. 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

from sys import stdin

input = stdin.readline

step = int(input())
score = [0] * (301)  # [0]*[step+1] => IndexError
d = [0] * (301)  # [0]*[step+1] => IndexError

i = 0
for i in range(step):
    score[i] = int(input())

d[0] = score[0]
d[1] = score[0] + score[1]
d[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, step + 1):
    d[i] = max(d[i - 3] + score[i - 1] + score[i], d[i - 2] + score[i])

print(d[step - 1])
