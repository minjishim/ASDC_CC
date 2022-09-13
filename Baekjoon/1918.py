# (7주차 : 스택) 후위 표기식

# isalpha() => 알파벳인지 확인
# isdigit() => 숫자인지 확인
# isalnum() => 알파벳 또는 숫자인지 확인

input = input()
stack = []
postfix = ''

# '('을 0으로 설정한 이유는 line 36을 위함('(' 다음에 오는 연산자들은 모두 stack에 들어가야 하므로, '('를 제일 낮은 값으로 설정)
prioty = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for input_index in input:
    # 피연산자(알파벳)인 경우, postfix(출력내용)에 추가
    if (input_index.isalpha()):
        postfix += input_index

    # '('인 경우, stack에 추가
    elif (input_index == '('):
        stack.append(input_index)

    # ')'인 경우
    elif (input_index == ')'):
        # stack 범위 내에서
        #'('가 나올 때까지 pop() 및 postfix(출력내용)에 추가
        while (stack and stack[-1] != '('):
            postfix += stack.pop()
        # '('를 pop() 처리
        stack.pop()

    # 그 외의 경우,
    else:
        # stack 범위 내에서
        # input_index의 우선순위가 stack[-1]의 우선순위보다 작거나 같을 경우에 pop() 및 postfix(출력내용)에 추가
        while (stack and prioty[input_index] <= prioty[stack[-1]]):
            postfix += stack.pop()
        # stack에 추가
        stack.append(input_index)

# stack에 남은 값들을 postfix(출력내용)에 추가
while stack:
    postfix += stack.pop()

# 출력
print(postfix)
