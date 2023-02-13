'''
백준 2635번. 수 이어가기
100 (입력)
(출력)
8
100 62 38 24 14 10 4 6  (음수는 버림.)
1. 첫번째 수 입력 받음.       int(input()) / 빈 리스트 생성.
2. 그 다음 수는 첫 번째 수보다 작은 수로 랜덤..? 절반 이상?
3. 맨처음 수에서 그 다음 수 뺀 수   first - second =
4. 뺄 위치를  마지막 수 바로 앞에 걸로 리셋  first = second
5. 반복하는 거 카운트 할 필요 없이 리스트에 놓고 len 출력 len(ans)
6. 마지막에 음수가 나오기 전에 스탑. if >= 0: append/ else: break
7. 리스트 빼고 숫자만 출력. *ans

'''
N = int(input())
ans = []       # 답 내줄 리스트

for i in range(1, N + 1):        # 주어진 수 다음부터 시작.
    first = N
    second = i
    tmp = [N, i]                 # 세팅먼저 해주고

    while True:
        next_num = first - second
        if next_num >= 0:
            tmp.append(next_num)    # 값을 더해줌.
            first = second
            second = next_num
        else:
            if len(tmp) > len(ans):     # 0보다 작아지면 끝내야 하니깐. 간편하게 옮겨줌.
                ans = tmp
            break                       #break 중요.
print(len(ans))
print(*ans)