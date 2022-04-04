n = int(input())
check = n #시간초과 방지, 초기 입력 값을 check 보관
count = 0

while True:
    result = n//10 + n%10 #십의자리 + 일의자리
    new = (n%10)*10 + result%10 #일의자리*10 + result나머지
    count = count + 1
    n = new #시간초과 방지, 입력 값 변환?
    if new == check: #새로운 값과 초기 입력 값 비교
        break
print(count)