aa=[]
bb=[]
value = 0

#aa리스트방 짝수 할당
for i in range(0,100):
    aa.append(value)
    value=value+2

#bb리스트방 aa리스트방의 값을 거꾸로 넣어줌
for i in range(0,100):
    bb.append(aa[99-i])

print("bb[0]에는 %d가 , bb[99]에는 %d가 있음 "%(bb[0],bb[99]))
