import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    # {'이름': 'James', '나이': 20, '취미': ['독서', '골프', '야구']}


# with 예시

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("Study Python hard")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
    # Study Python hard
