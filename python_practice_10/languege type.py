num = input("문자열 입력:")

if num.isdigit() == True:
    print("숫자입니다")
elif num.isalpha() ==True:
    print("문자입니다.")
elif num.isalnum() == True:
    print("숫자와 문자로 섞여 있습니다.")
else:
    print("모르겠습니다")
