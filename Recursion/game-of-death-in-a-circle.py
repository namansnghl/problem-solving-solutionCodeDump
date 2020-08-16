# https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle/0
# code
def safe(lst, k, pos):
    if len(lst) == 1:
        return
    pos = (pos+k) % len(lst)
    lst.pop(pos)
    safe(lst, k, pos-1)


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    lst = [x for x in range(1, n+1)]
    safe(lst, k, -1)
    print(lst[0])
