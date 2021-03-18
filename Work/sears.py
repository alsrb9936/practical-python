# sears.py

bill_thickness = 0.11 * 0.001    # 미터(0.11 mm)
sears_height   = 442             # 높이(미터)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

# 몇 번째 행에 오류가 났는가? line 10
# 무엇이 잘못되었는가? days 라는 이름의 변수가 선언되지 않았다 (잘못된 변수 이름기입 ,오타)
# 오류수정 days -> day