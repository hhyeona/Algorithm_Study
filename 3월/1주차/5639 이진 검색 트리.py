'''
전위 순회 입력 
후위 순회 출력
재귀?
입력: 첫번째 루트/ 루트보다 작은 것들 왼쪽/ 큰 건 오른쪽.
출력: 왼쪽/ 오른쪽/ 루트 순으로 반환.
root를 기준으로 구간을 나눠야 해서, index가 중요.
'''
import sys
sys.setrecursionlimit(10**5)   # 재귀 깊이 늘려주는 설정.

#[50, 30, 24, 5, 28, 45, 98, 52, 60]
#[30, 24, 5, 28, 45]
#[98, 52, 60]

def post(s, e):           # 파라미터로 시작점과 끝점 index.
    if s > e:        # 범위를 벗어나면 안되니까. (ex)98 이후로 오른쪽 자식 노드들이 없을 경우 )
        return

    root = lst[s]          # 일반화 (루트 갱신)
    num = 0                #flag 지우고 애초에 num = e+1 로 해도 됨.
    flag = 0               # 오른쪽 자식들이 없을 경우 확인해주려고 
    for idx in range(s+1,e+1):
        if lst[idx] > lst[s]:
            num = idx
            flag = 1
            break

    if flag == 0:         # 오른쪽 자식이 없다면, (post(s+1,num-1)가 52,60이면 8/7 이 되어버려서 자동적으로 return 만들어준 것)
        num = e+1

    post(s+1,num-1)          #왼쪽 자식들 호출
    post(num,e)              #오른쪽 자식들 호출
    print(root)              # 후위순회로 출력.

lst = []                            #[50, 30, 24, 5, 28, 45, 98, 52, 60]
while True:                         # 입력 길이가 정해져 있지 않으므로 예외처리로 입력받음.
    try:
        node = int(input())         # = lst.append(int(input())) 해도 됨.
        lst.append(node)            # 하나씩 입력받은 걸 리스트에 더해줌.

    except:
        break


N = len(lst)
post(0,N-1)

