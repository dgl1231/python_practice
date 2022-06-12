import operator

trainDic,trainList = {},[]

trainDic={'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든'}

#키를 기준으로 하는경우 :0, 값을 기준으로 하는 경우 :1
trainList = sorted(trainDic.items(),key=operator.itemgetter(1))

print(trainList)
