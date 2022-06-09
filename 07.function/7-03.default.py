def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}".format(name, age, main_lang))


profile("James", 20, "Python")
profile("Mary", 25, "C++")


# 같은 학교, 같은 학년, 같은 반 수업

def profile(name, age=17, main_lang="Python"):
    print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}".format(name, age, main_lang))


profile("Linda")
profile("David")
