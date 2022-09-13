# (2주차 : 그리디) 회문

i = 0
t = int(input())
palindrome_types = []  # 0 회문, 1 유사회문, 2 일반문자열

for i in range(0, t, 1):
    palindrome = 0
    t_types = list(input())
    first, last = 0, len(t_types) - 1

    while (first < last):
        # 같다면 계속해서 끝과 끝의 배열 인덱스 값을 증가하면서 비교
        if (t_types[first] == t_types[last]):
            first = first + 1
            last = last - 1

        # 다르다면
        else:
            if (first + 1 < last):
                # 동일한 부분(앞) 지우고 저장
                first_t_types = t_types[:first] + t_types[first + 1:]
                # [:] 와 [::-1], 즉 배열과 역순배열이 같다면
                if (first_t_types[:] == first_t_types[::-1]):
                    palindrome = 1
                    break

            if (first < last - 1):
                # 동일한 부분(뒤) 지우고 저장
                last_t_types = t_types[:last] + t_types[last + 1:]
                # [:] 와 [::-1], 즉 배열과 역순배열이 같다면
                if (last_t_types[:] == last_t_types[::-1]):
                    palindrome = 1
                    break

            palindrome = 2
            break
    palindrome_types.insert(i, palindrome)

for i in range(0, t, 1):
    print(palindrome_types[i])
