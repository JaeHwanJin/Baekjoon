hour, minute, second = map(int, input().split())
time = int(input())

second += time
minute += second//60
hour += minute//60

print(hour%24, minute%60, second%60)