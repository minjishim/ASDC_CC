# (4주차 그리디+구현) 롤러코스터

# 행(r), 열(c) 입력받기
r, c = map(int, input().split())

# 전체 맵 정보 입력받기(기쁨)
array = []
for i in range(r):
    array.append(list(map(int, input().split())))


#-------------------------------------------------------------------------
# 행이 홀수일 때
def r_odd():
    # 정수형 변수(r,c)가 함수 바깥에서 선언된 전역변수이기 때문에 global 키워드 사용
    global r, c
    print(
        # 열의 갯수보다 하나 적게 R/L 이동 후 아래로 이동
        # 전체 행을 2로 나눈 몫만큼 반복(전체 행이 1인 경우에는 수행하지 않음)
        ((('R' * (c - 1)) + 'D') + ('L' * (c - 1)) + 'D') * (r // 2)
        # 행을 2로 나눈 나머지가 있는 경우 이동(전체 행이 1인 경우 포함)
        + ('R' * (c - 1)))


#-------------------------------------------------------------------------
# 열이 홀수일 때
def c_odd():
    # 정수형 변수(r,c)가 함수 바깥에서 선언된 전역변수이기 때문에 global 키워드 사용
    global r, c
    print(
        # 행의 갯수보다 하나 적게 D/U 이동 후 아래로 이동
        # 전체 열을 2로 나눈 몫만큼 반복(전체 열이 1인 경우에는 수행하지 않음)
        ((('D' * (r - 1)) + 'R') + ('U' * (r - 1)) + 'R') * (c // 2)
        # 열을 2로 나눈 나머지가 있는 경우 이동(전체 열이 1인 경우 포함)
        + ('D' * (r - 1)))


#-------------------------------------------------------------------------
# 행과 열이 모두 짝수일 때
def rc_even():
    global r, c
    # 기쁨이 작은 곳을 찾기 위한 값과 위치 초기화
    low_pleasure = 1000
    low_pleasure_position = [-1, -1]

    # 기쁨이 작은 곳을 찾기(체스판 기준, (0,0) 위치와 다른 색깔인 부분에서)
    for r_index in range(r):
        # 행이 짝수일 때
        if (r_index % 2 == 0):
            # 열이 홀수인 경우에만 low_pleasure 위치 찾기
            for c_index in range(1, c, 2):
                if low_pleasure > array[r_index][c_index]:
                    low_pleasure = array[r_index][c_index]
                    low_pleasure_position = [r_index, c_index]
        # 행이 홀수일 때
        else:
            # 열이 짝수인 경우에만 low_pleasure 위치 찾기
            for c_index in range(0, c, 2):
                if low_pleasure > array[r_index][c_index]:
                    low_pleasure = array[r_index][c_index]
                    low_pleasure_position = [r_index, c_index]

    # 기쁨이 제일 작은 곳이 있기 전까지 이동(D R U R 이동)
    # 제외할 위치가 있는 열을 2로 나눈 몫만큼 반복
    move = ((('D' * (r - 1)) + 'R') +
            ('U' * (r - 1)) + 'R') * (low_pleasure_position[1] // 2)

    # 제외할 위치가 있는 열(position[1])을 2로 나눈 몫만큼 이동한 후의 위치 설정
    now_r = 0
    now_c = (low_pleasure_position[1] // 2) * 2

    # 마지막 열의 위치 설정
    last_c = ((low_pleasure_position[1] // 2) * 2) + 1

    # 현재 위치가 마지막 열이 아니고, 마지막 행이 아닐 때까지 이동
    while ((now_c != last_c) or (now_r != r - 1)):
        # 현재 위치가 마지막 열보다 왼쪽이고
        # 현재 위치의 오른쪽이 가장 적은 기쁨이 있는 위치가 아닌 경우
        if ((now_c < last_c) and ([now_r, last_c] != low_pleasure_position)):
            now_c += 1
            move += 'R'
        # 현재 위치가 마지막 열이고
        # 현재 위치의 왼쪽이 가장 적은 기쁨이 있는 위치가 아닌 경우
        elif ((now_c == last_c)
              and ([now_r, last_c - 1] != low_pleasure_position)):
            now_c -= 1
            move += 'L'
        # 현재 위치가 마지막 행이 아닐 경우
        if (now_r != r - 1):
            now_r += 1
            move += 'D'

    move += (('R' + 'U' * (r - 1)) +
             ('R' + 'D' * (r - 1))) * ((c - low_pleasure_position[1] - 1) // 2)

    print(move)


#-------------------------------------------------------------------------

if ((r % 2) == 1):
    r_odd()
elif ((c % 2) == 1):
    c_odd()
else:
    rc_even()
