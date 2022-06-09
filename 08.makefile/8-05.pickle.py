# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해 주는 것

import pickle

# pickle 을 통해 저장
profile_file = open("profile.pickle", "wb")  # wb : write binary
profile = {"이름": "James", "나이": 20, "취미": ["독서", "골프", "야구"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 정보를 profile_file 에 저장
profile_file.close()

# pickle 을 통해 불러오기
profile_file = open("profile.pickle", "rb")  # rb : read binary
profile = pickle.load(profile_file)  # profile_file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
