# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# ex. http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + '!' 로 구성

# 생성된 비밀번호 : nav51!

url = "http://naver.com"
password = url[7:10] + str(len(url[7:12])) + str(url.count("e")) + "!"
print("\"{0}\" 의 비밀번호는 \"{1}\" 입니다." .format(url, password))

print()


# 답

url = "http://google.com"
# 규칙 1 : http:// 를 공백으로 바꾸기
url_name = url.replace("http://", "")
# 규칙2 : url_name[0:5] 직전까지
url_name = url_name[:url_name.index(".")]
# 규칙 3 :
password = url_name[:3] + str(len(url_name)) + str(url_name.count("e")) + "!"
print("\"{0}\" 의 비밀번호는 \"{1}\" 입니다." .format(url, password))
