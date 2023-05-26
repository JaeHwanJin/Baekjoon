def solution(n, k):
    ans = 0
    ans += (12000*n + 2000*k)
    ans -= n//10 * 2000
    return ans