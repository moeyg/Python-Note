resident_number = "000111-4444440"

print("Sex : " + resident_number[8])
print("Year : " + resident_number[0:2])  # 0부터 2 직전까지
print("Month : " + resident_number[2:4])
print("Date : " + resident_number[4:6])

print("Birth Date : " + resident_number[:6])  # 처음부터 6 직전까지
print("Address Info : " + resident_number[7:])  # 7부터 마지막까지
print("Address Info (from behind) : " + resident_number[-7:])  # 맨 뒤에서부터 끝까지
