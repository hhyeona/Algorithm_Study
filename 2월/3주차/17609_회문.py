'''
문자열. 
회문 : 0
유사 회문(한 문자 삭제) : 1
둘 다 아니면 : 2

7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc
'''
# T = int(input())
# word = list(input() for _ in range(T))
#
#
# cnt = int(len(word)//2)
#
# for _ in range(len(word)):
#     left = [word[x] for x in range(0, cnt)]
#     right = [word[-x] for x in range(1, cnt+1)]
#     if left == right:
#         print(0)
#     else:
#         print(2)

# while left < right:
#     if left == right:
#         return 0
#
#     elif left != right:
#         left = [word[x+1] for x in range(0, cnt)]
#         right = [word[-x-1] for x in range(1, cnt + 1)]
#         if left == right:
#             return 1
#
#     else:
#         return 2
def check(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            l_remove = check2(word, l + 1, r)
            r_remove = check2(word, l, r - 1)
            if (l_remove or r_remove):
                return 1
            else:
                return 2
    return 0


def check2(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


T = int(input())
for _ in range(T):
    word = list(input() for _ in range(T))

    l = 0
    r = len(word) - 1

    print(check(word, l, r))



