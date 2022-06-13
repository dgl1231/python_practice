#함수선언
def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1+v2
    elif op== '-':
        result = v1-v2
    elif op== '*':
        result = v1*v2
    elif op== '/':
        result = v1/v2
    elif op== '**':
        result = v1**v2
        
    return result


#메인
var1 = int(input("첫수 입력:"))
oper = input("계산을 입력하세요(+,-,*,/,**) : ")
var2 = int(input("두번째수 입력:"))

if (oper == '/') and (var2 == 0):
    print("0으로는 나누면 안된다.")
else:
    res = calc(var1,var2,oper)    
    print("## 계산기 : %d %s %d = %d"%(var1,oper,var2,res))


