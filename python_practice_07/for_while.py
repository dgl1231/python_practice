i,hap = 0,0
'''
for i in range(0,101,2):
    hap = hap + i

print("0과 100사이에 있는 짝수")
'''


while i < 101:
    if i % 2 == 0:
        hap += i
    i = i + 1

print("0과 100사이에 있는 짝수 : %d" %hap)
