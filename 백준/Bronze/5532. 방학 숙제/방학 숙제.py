import math
vacation = int(input())
korean = int(input())
Math = int(input())
korean_time = int(input())
Math_time = int(input())

korean_date = math.ceil(korean/korean_time)
Math_date = math.ceil(Math/Math_time)
if korean_date > Math_date :
    print(vacation - korean_date)
else :
    print(vacation - Math_date)