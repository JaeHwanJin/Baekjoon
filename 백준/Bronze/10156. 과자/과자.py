cookie_price, cookie_cnt, my_money = map(int, input().split())

if cookie_price * cookie_cnt > my_money :
    print(cookie_price * cookie_cnt - my_money)
else:
    print(0)