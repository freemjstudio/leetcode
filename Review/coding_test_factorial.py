# 1. for 반복문 사용하기

N = int(input("number:"))
'''
result = 1
for i in range(1, N+1):
    result *= i

print(result)

'''



'''
dp = [0] * (N+1) # dp 에 0 등장하는 개수 저장하기
for i in range(N):
    dp[i] = dp[i//5] + i//5
print(dp[N])
'''
