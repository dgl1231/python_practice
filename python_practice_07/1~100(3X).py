hap,i=0,0

for i in range(1,101):
    if i%3==0:
        continue
    hap = hap+i

print("1~100까지의 합계(3의배수 제거) : %d" %hap)
