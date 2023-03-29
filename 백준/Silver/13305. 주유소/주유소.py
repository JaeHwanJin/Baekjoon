N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

print(sum(length)*((int(sum(price))//len(price))))