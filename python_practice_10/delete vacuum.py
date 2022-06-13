inStr = " 한글 Python 프로그래밍  "
outStr=""

for i in range (0,len(inStr)):
    if inStr[i] != ' ':
        outStr = outStr + inStr[i]

print("원래 문자열 ==>" + '[' + inStr+ ']')
print("공백 삭제된 문자열 ==>" + '[' + outStr + ']')
