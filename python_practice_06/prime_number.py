#변수
numCount =0

#메인코드
num1 = int(input("***숫자를 입력하세요 : "))\

for i in range(1,num1+1):
    if (num1 % i ) ==0:
        numCount = numCount +1

if numCount ==2:
    print("%d는 소수입니다."%num1)
else :
    print("%d는 소수가 아닙니다."%num1)
