oldList = ['짜장면', '탕수육', '군만두']
#메모리 공간을 복사하는 방법 2가지중 한가지 적용하세요.
#new List = oldList[:]
newList = oldList.copy()
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)
