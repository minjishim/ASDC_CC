# (15주차 : 다이나믹 프로그래밍) 24416 - 피보나치 수 1
''' 오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}

피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
'''

from sys import stdin


def fib(n):
    if ((n == 1) or (n == 2)):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    # (n+1)로 곱하는 이유는 리스트 요소는 0부터 시작하지만, n은 1부터 시작하므로
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    count = 0
    for i in range(3, n + 1):
        count += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    return count


n = int(input())
print(fib(n), fibonacci(n))
