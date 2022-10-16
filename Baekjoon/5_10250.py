# (5주차 : 구현) ACM 호텔

t = int(input())  # t: 테스트 케이스

for t_index in range(t):
    # h, w, n : 층 수, 방 수, 몇번째 손님
    h, w, n = map(int, input().split())

    # 사람 수 / 층 수 = 몇 번째 층(h)인지
    # (사람 수 / 층 수)의 몫 + 1 = 몇 번째 방(w)인지
    if ((n % h) != 0):
        room_h = n % h
        room_w = (n // h) + 1

    # (n % h) == 0, 즉, 마지막 층에 위치해야 하는 손님일 때
    else:
        room_h = h
        room_w = (n // h)

    print((room_h * 100) + room_w)
