# PYTHON 의 any() 함수
# list 의 원소를 필터링하거나 조건 검사하는데 사용

test = [2,5,3,6,7,8,9,1,10]

check = any(x > 5 for x in test)
print("5보다 큰 어떠한 원소가 있는가 ? " + str(check))