# https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
res = []


def stringPermute(strList, left, right):
    if left == right:
        res.append("".join(strList))
    else:
        for i in range(left, right+1):
            strList[i], strList[left] = strList[left], strList[i]
            stringPermute(strList, left+1, right)
            strList[i], strList[left] = strList[left], strList[i]  # backTrack


for _ in range(int(input())):
    res = []
    string = input()
    pattern = list(string)
    stringPermute(pattern, 0, len(string)-1)
    print(*sorted(res))
