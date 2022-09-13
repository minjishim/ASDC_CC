# (3주차 : 그리디) ATM

def cal_time(person):
    #index_i : 인덱스, time : 지금 걸리는 시간, total_time : 현재까지 총 걸리는 시간
    index_i, time, total_time = 0, 0, 0

    #person_time : 각 사람마다 걸리는 시간, 공백 기준으로 split해서 list로 입력
    person_time = list(map(int, input().split()))

    # sort, sorted
    person_time.sort()

    #시간 계산
    for index_i in person_time:
        time = time + index_i
        total_time = total_time + time

    #출력
    print(total_time)


#-----main-----
#person : 총 사람 숫자 입력
person = int(input())
#person을 매개변수로 한 cal_time 함수 호출
cal_time(person)
