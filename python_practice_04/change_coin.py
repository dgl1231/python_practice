#변수
money,c500,c100,c50 ,c10 = 0,0,0,0,0

#메인코드
money = int(input("교환할 돈은 얼마인가요? : "))

c500 = money//500
money =money %500

c100 = money //100
money %=100

c50 = money//50
money %=50

c10 =money // 10
money %= 10

print("\n 500원짜리 ==> %d개" %c500)
print("\n 100원짜리 ==> %d개" %c100)
print("\n 50원짜리 ==> %d개" %c50)
print("\n 10원짜리 ==> %d개" %c10)
print("\n 바꾸지 못한 잔돈 ==> %d원" %money)
