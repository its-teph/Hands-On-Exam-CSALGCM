"""
This function solves one query XP value.

Parameters:
n : int - number of levels
xps : array-like - array containing the required xp values for each level
q_i : int - xp value to compute the level of

Returns:
A string containing the answer (either level or "Wait for it")
"""
def solve(n,xps,q_i):
    # TODO
    low = 0
    high = n
    
    while low < high:
        mid = (low + high) // 2
        if q_i < xps[mid]:
            high = mid
        else:
            low = mid + 1

    if high == 0:
        return "Wait for it"
    else: 
        return high
    #pass

n,q = list(map(int,input().strip().split(" ")))
xps = [int(input()) for i in range(n)]
qs = [int(input()) for i in range(q)]

ans = []

for q_i in qs:
    ans.append(solve(n,xps,q_i))

print("\n".join(list(map(str,ans))))