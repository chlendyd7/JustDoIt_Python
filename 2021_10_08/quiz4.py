#quiz) 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰, 추첨 프로그램을 작성
from random import*
users = range(1, 21) # 1부터 20까지 숫자 생성 type은 range
users = list(users)
shuffle(users)#섞어줌

winners = sample(users, 4)
print(" -- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")
