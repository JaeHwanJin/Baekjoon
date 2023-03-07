import math

up, down, top = map(int, input().split())
day = (top-down)/(up-down) # 정상에 도달 했을때 미끄러지지 않는것을 고려
print(math.ceil(day))