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
첫 번째 수n의 범위가인  30,000이하의 양의 정수이므로 완전탐색을 해도 충분히 제한 시간내에 할 수 있음.
n~1 까지의 모든 수들을 두 번째 수로 선택한 후에 아래 과정을 반복함. f
더
'''
N = int(input())
ans = []       # 답 내줄 리스트

for i in range(1, N + 1):    # 완전 탐색 시작.
    first = N
    second = i
    tmp = [N, i]       # f-s 값 넣어줌.

    while True:
        next_num = first - second
        if next_num >= 0:
            tmp.append(next_num)    # 값을 더해줌.
            first = second          # 다음 숫자를 갱신.
            second = next_num
        else:
            if len(tmp) > len(ans):     # 0보다 작아지면 끝내야 하니깐. 간편하게 옮겨줌.
                ans = tmp
            break                       #break 중요.
print(len(ans))
print(*ans)           # 결국 제일 len 길이가 큰 것이 최종 답이 됨.